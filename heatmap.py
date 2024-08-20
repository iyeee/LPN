import os
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from model import three_view_net
from utils import load_network
import yaml
import argparse
import torch
import torch.nn as nn
import torchvision
from torchvision import datasets, models, transforms
from PIL import Image
os.environ["CUDA_VISIBLE_DEVICES"] = '2'
parser = argparse.ArgumentParser(description='Training')

parser.add_argument('--data_dir',default='/data/modanqi/datasets/data/test',type=str, help='./test_data')
parser.add_argument('--name', default='final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001', type=str, help='save model path')
parser.add_argument('--batchsize', default=1, type=int, help='batchsize')

opt = parser.parse_args()

config_path = os.path.join('./model',opt.name,'opts.yaml')
with open(config_path, 'r') as stream:
        config = yaml.load(stream,Loader=yaml.FullLoader)
opt.fp16 = config['fp16']
# opt.PCB = config['PCB']
opt.stride = config['stride']
opt.block = config['block']
opt.views = config['views']

if 'h' in config:
    opt.h = config['h']
    opt.w = config['w']
if 'nclasses' in config: # tp compatible with old config files
    opt.nclasses = config['nclasses']
else:
    opt.nclasses = 751


class simam_module(torch.nn.Module):
    def __init__(self, channels = None, e_lambda = 1e-4):
        super(simam_module, self).__init__()

        self.activaton = nn.Sigmoid()
        self.e_lambda = e_lambda

    def __repr__(self):
        s = self.__class__.__name__ + '('
        s += ('lambda=%f)' % self.e_lambda)
        return s

    @staticmethod
    def get_module_name():
        return "simam"

    def forward(self, x):

        b, c, h, w = x.size()
        
        n = w * h - 1

        x_minus_mu_square = (x - x.mean(dim=[2,3], keepdim=True)).pow(2)
        y = x_minus_mu_square / (4 * (x_minus_mu_square.sum(dim=[2,3], keepdim=True) / n + self.e_lambda)) + 0.5
        #torch.Size([8, 768, 8, 8])
        return y
def heatmap2d(img, arr):
    # fig = plt.figure()
    # ax0 = fig.add_subplot(121, title="Image")
    # ax1 = fig.add_subplot(122, title="Heatmap")
    # fig, ax = plt.subplots(）
    # ax[0].imshow(Image.open(img))
    # binary_arr = np.where(arr >= np.median(arr), 1, 0)
    # arr=binary_arr
    plt.figure()
    heatmap = plt.imshow(arr, cmap='viridis')
    plt.axis('off')
    plt.colorbar()
    # fig.colorbar(heatmap, fraction=0.046, pad=0.04)
    #plt.show()
    plt.savefig('heatmap_dbase')
def improved_hfs_mo_with_grouping2(x, num_groups=4):
    # x = x.permute(0, 3, 1, 2)

    b, c, h, w = x.size()
    group_channels = c // num_groups  # 每个组的通道数

    # 初始化一个空的列表来存放应用了掩码的分组结果
    grouped_x_masked = []

    # 对每个分组进行处理
    for i in range(num_groups):
        # 提取当前分组的通道
        group = x[:, i*group_channels:(i+1)*group_channels, :, :]

        # 计算当前分组的平均值
        avg = group.mean(1)
        thr = avg.view(b, -1).sum(-1) / (h * w)
        mask = (avg > thr.unsqueeze(-1).unsqueeze(-1)).float()

        # # 应用sigmoid函数和调整
        # mask = torch.sigmoid(mask)+0.5
        # mask += 1.5
        mask=mask+0.3



        # 应用掩码到当前分组
        masked_group = group * mask.unsqueeze(1)

        # 将处理后的分组添加到列表中
        grouped_x_masked.append(masked_group)

    # 重新排列维度以符合原始输入格式
    final_result = torch.cat(grouped_x_masked, dim=1)
    # final_result = final_result.permute(0, 2, 3, 1)

    return final_result
data_transforms = transforms.Compose([
        transforms.Resize((opt.h, opt.w), interpolation=3),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# image_datasets = {x: datasets.ImageFolder( os.path.join(opt.data_dir,x) ,data_transforms) for x in ['satellite']}
# dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], batch_size=opt.batchsize,
#                                              shuffle=False, num_workers=1) for x in ['satellite']}

# imgpath = image_datasets['satellite'].imgs
# print(imgpath)
# imgname = 'gallery_drone/0719/image-28.jpeg'
# imgname = 'query_drone/0736/image-28.jpeg'
# imgname = '150/gallery_drone/0042/1.jpg'
imgname='gallery_satellite/0736/0736.jpg'
imgpath = os.path.join(opt.data_dir,imgname)
img = Image.open(imgpath)
img = data_transforms(img)
img = torch.unsqueeze(img,0)
print(img.shape)
model, _, epoch = load_network(opt.name, opt)

model = model.eval().cuda()

# data = next(iter(dataloaders['satellite']))
# img, label = data
with torch.no_grad():
    # sia=simam_module(512)
    x = model.model_3.model.conv1(img.cuda())
    x = model.model_3.model.bn1(x)
    x = model.model_3.model.relu(x)
    x = model.model_3.model.maxpool(x)
    x = model.model_3.model.layer1(x)
    x = model.model_3.model.layer2(x)
    x = model.model_3.model.layer3(x)
    output = model.model_3.model.layer4(x)
    # output=improved_hfs_mo_with_grouping2(output,num_groups=4)
    # output =sia(output)
    output = nn.AdaptiveMaxPool2d((8, 8))(output)
print(output.shape)
heatmap = output.squeeze().sum(dim=0).cpu().numpy()
print(heatmap.shape)
#test_array = np.arange(100 * 100).reshape(100, 100)
# Result is saved tas `heatmap.png`
heatmap2d(imgpath,heatmap)