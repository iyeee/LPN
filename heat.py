import os

import cv2
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from utils import load_network
import yaml
import argparse
import torch
from torchvision import datasets, models, transforms
from PIL import Image
os.environ["CUDA_VISIBLE_DEVICES"] = '0'
parser = argparse.ArgumentParser(description='Training')
import math

# parser.add_argument('--data_dir',default='/data/modanqi/datasets/data/test',type=str, help='./test_data')
# parser.add_argument('--name', default='final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001', type=str, help='save model path')
# parser.add_argument('--batchsize', default=1, type=int, help='batchsize')
# parser.add_argument('--checkpoint',default="/data/modanqi/projects/new/LPN/model/final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001/net_119.pth", help='weights' )

parser.add_argument('--data_dir',default='/data/modanqi/datasets/data/test',type=str, help='./test_data')
parser.add_argument('--name', default='final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001', type=str, help='save model path')
parser.add_argument('--batchsize', default=1, type=int, help='batchsize')

opt = parser.parse_args()

config_path = os.path.join('./model',opt.name,'opts.yaml')
with open(config_path, 'r') as stream:
    config = yaml.load(stream,Loader=yaml.FullLoader)
# opt.stride = config['stride']
opt.views = config['views']
# opt.transformer = config['transformer']
# opt.pool = config['pool']
# opt.LPN = config['LPN']
opt.block = config['block']
opt.nclasses = config['nclasses']
# opt.droprate = config['droprate']
opt.share = config['share']

if 'h' in config:
    opt.h = config['h']
    opt.w = config['w']
if 'nclasses' in config: # tp compatible with old config files
    opt.nclasses = config['nclasses']
else:
    opt.nclasses = 751


def heatmap2d(img, arr):
    # fig = plt.figure()
    # ax0 = fig.add_subplot(121, title="Image")
    # ax1 = fig.add_subplot(122, title="Heatmap")
    # fig, ax = plt.subplots(）
    # ax[0].imshow(Image.open(img))
    plt.figure()
    heatmap = plt.imshow(arr, cmap='viridis')
    plt.axis('off')
    # fig.colorbar(heatmap, fraction=0.046, pad=0.04)
    #plt.show()
    plt.savefig('heatmap_dbase')

data_transforms = transforms.Compose([
        transforms.Resize((opt.h, opt.w), interpolation=3),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

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
        mask=mask+1



        # 应用掩码到当前分组
        masked_group = group * mask.unsqueeze(1)

        # 将处理后的分组添加到列表中
        grouped_x_masked.append(masked_group)

    # 重新排列维度以符合原始输入格式
    final_result = torch.cat(grouped_x_masked, dim=1)
    # final_result = final_result.permute(0, 2, 3, 1)

    return final_result
def normalization(data):
    _range = np.max(data) - np.min(data)
    return (data - np.min(data)) / _range

# model = load_network(opt)
model, _, epoch = load_network(opt.name, opt)
print(opt.data_dir)
# for i in ["0001","0002","0003","0004","0005","0006","0007","0008","0009","0010","0011","0012","0013","0014","0015","0016","0017","0018","0019","0020","0021","0022","0023","0024","0025","0026","0027","0028","0029","0030","0031","0032","0033","0034","0035","0036","0037","0038","0039","0040","0041","0042","0043","0044","0045","0046","0047","0048","0049","0050","0051","0052","0053","0054","0055","0056","0057","0058","0059","0060","0061","0062","0063","0064","0065","0067","0068","0069","0070","0071"]:
for i in ["0005"]:    
    print(i)
    # imgpath = os.path.join(opt.data_dir,"gallery_drone/"+i)
    # imgpath = os.path.join(imgpath, "image-28.jpeg")
    imgpath = os.path.join(opt.data_dir,"query_satellite/"+i)
    imgpath = os.path.join(imgpath, i+".jpg")
    print(imgpath)
    img = Image.open(imgpath)
    img = data_transforms(img)
    img = torch.unsqueeze(img,0)


    model = model.eval().cuda()

    with torch.no_grad():
        x = model.model_3.model.conv1(img.cuda())
        x = model.model_3.model.bn1(x)
        x = model.model_3.model.relu(x)
        x = model.model_3.model.maxpool(x)
        x = model.model_3.model.layer1(x)
        x = model.model_3.model.layer2(x)
        x = model.model_3.model.layer3(x)
        output = model.model_3.model.layer4(x)
        output=improved_hfs_mo_with_grouping2(output,num_groups=4)
        # features,_ = model.model_1.transformer(img.cuda())
        # pos_embed = model.model_1.transformer.pos_embed
        # part_features = features[:,1:]
        # part_features = part_features.view(part_features.size(0),int(math.sqrt(part_features.size(1))),int(math.sqrt(part_features.size(1))),part_features.size(2))
        # output = part_features.permute(0,3,1,2)

    heatmap = output.squeeze().sum(dim=0).cpu().numpy()
    # print(heatmap.shape)
    # print(heatmap)
    # heatmap = np.mean(heatmap, axis=0)
    #
    # heatmap = np.maximum(heatmap, 0)
    heatmap = normalization(heatmap)
    img = cv2.imread(imgpath)  # 用cv2加载原始图像
    heatmap = cv2.resize(heatmap, (img.shape[1], img.shape[0]))  # 将热力图的大小调整为与原始图像相同
    heatmap = np.uint8(255 * heatmap)  # 将热力图转换为RGB格式
    heatmap = cv2.applyColorMap(heatmap, 2)  # 将热力图应用于原始图像model.py
    superimposed_img = heatmap * 0.6 + img  # 这里的0.4是热力图强度因子
    if not os.path.exists("heatout"):
        os.mkdir("./heatout/s")
    cv2.imwrite("./heatout/s"+i+".jpg", superimposed_img)