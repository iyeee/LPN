+ **Rk-Net （train  batchsize=8 )**

  + sattlite->drone 1->3

    + 0usam RK-Net_0usam   
      + Recall@1:75.46 Recall@5:83.02 Recall@10:86.02 Recall@top1:97.00 AP:62.42(epoch=999）
      + Recall@1:76.18 Recall@5:83.31 Recall@10:86.88 Recall@top1:96.86 AP:62.41(epoch=360)
    + 0.5usam RK-Net_0.5usam 
      + Recall@1:74.32 Recall@5:82.74 Recall@10:86.16 Recall@top1:97.57 AP:61.76(epoch=999）
      + Recall@1:75.46 Recall@5:82.88 Recall@10:86.73 Recall@top1:97.43 AP:61.63(epoch=360)
    + 1usam RK-Net_usam 
      + Recall@1:75.61 Recall@5:81.31 Recall@10:85.16 Recall@top1:97.43 AP:61.25(epoch=999）
      + Recall@1:73.89 Recall@5:81.17 Recall@10:84.02 Recall@top1:97.43 AP:59.68(epoch=360)
    + 2usam RK-Net_2usam 
      + Recall@1:70.33 Recall@5:78.46 Recall@10:80.46 Recall@top1:97.00 AP:57.96(epoch=999)
      + Recall@1:70.19 Recall@5:77.32 Recall@10:80.17 Recall@top1:96.86 AP:57.18(epoch=360)
    + ResSpatialAttention RK-Net_usam_ResSpatialAttention 
      + Recall@1:74.89 Recall@5:80.88 Recall@10:84.45 Recall@top1:97.57 AP:60.53  (epoch=360)

  + drone->satellite 3->1

    + 0usam  RK-Net_0usam 
      + Recall@1:62.11 Recall@5:80.68 Recall@10:85.97 Recall@top1:86.61 AP:66.35(epoch=999）
      + Recall@1:62.76 Recall@5:81.50 Recall@10:86.68 Recall@top1:87.41 AP:67.02(epoch=360)
    + 0.5usam RK-Net_0.5usam 
      + Recall@1:60.77 Recall@5:80.20 Recall@10:85.66 Recall@top1:86.35 AP:65.17(epoch=999）
    + 1usam RK-Net_usam 
      + Recall@1:62.50 Recall@5:82.00 Recall@10:87.21 Recall@top1:87.80 AP:66.90(epoch=999）
      + Recall@1:61.68 Recall@5:81.33 Recall@10:86.92 Recall@top1:87.48 AP:66.13(epoch=360)
    + 2usam RK-Net_2usam  
      + Recall@1:56.34 Recall@5:76.28 Recall@10:82.38 Recall@top1:83.12 AP:60.92(epoch=999）
      + Recall@1:55.67 Recall@5:75.62 Recall@10:81.67 Recall@top1:82.38 AP:60.22(epoch=360)
    + ResSpatialAttention RK-Net_usam_ResSpatialAttention
      + Recall@1:60.09 Recall@5:79.80 Recall@10:85.39 Recall@top1:86.18 AP:64.55  (epoch=360)

    

    

    

    

    

    

+ **lpn  （train batchsize=8 )**

  + sattlite->drone 1->3

    +  final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001_5

      + Recall@1:84.74 Recall@5:90.01 Recall@10:91.30 Recall@top1:98.72 **AP:74.02** (epoch=360）
      + **Recall@1:85.31** Recall@5:90.16 Recall@10:92.01 Recall@top1:98.15 AP:73.80(epoch=160)

    + 0.5usam final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001_0.5usam

      + Recall@1:85.16 Recall@5:89.73 Recall@10:91.87 Recall@top1:98.43 AP:73.55(epoch=360）

    + 1usam  final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001_usam5

      + Recall@1:84.88 Recall@5:90.30 Recall@10:91.16 Recall@top1:98.57 AP:73.73(epoch=360）

    + 2usam  final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001_doubleUsam2

      + Recall@1:84.02 Recall@5:89.44 Recall@10:92.44 Recall@top1:99.29 AP:73.03(epoch=360）

    + SpatialAttention

      final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001_SpatialAttention

      + Recall@1:84.88 Recall@5:89.30 Recall@10:91.30 Recall@top1:98.57 AP:73.65(epoch=360）

    + ResSpatialAttention final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001_ResSpatialAttention

      + **Recall@1:85.73** Recall@5:89.87 Recall@10:91.73 Recall@top1:98.57 **AP:75.50**(epoch=360）

    + [1,2,3,4,5]CBAM   final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001_5CBAM

      + Recall@1:84.31 Recall@5:89.59 Recall@10:91.44 Recall@top1:98.86 AP:73.39 (epoch=160)

    + [1,2,3,4,5]final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001_ResSpatialAttention12345

      + Recall@1:83.88 Recall@5:89.02 Recall@10:90.30 Recall@top1:98.57 AP:72.48(epoch=160)

    + [1,2]final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001_ResSpatialAttention12

      + **Recall@1:85.45** Recall@5:90.58 Recall@10:92.58 Recall@top1:98.72 AP:73.64(epoch=160)

    + [CBAM1T]final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001_CBAM1T

      + Recall@1:85.16 Recall@5:89.59 Recall@10:92.58 Recall@top1:98.29 AP:73.56(epoch=160)

    + [CBAM15T]final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001_CBAM15T

      + Recall@1:84.88 Recall@5:90.01 Recall@10:92.01 Recall@top1:98.86 **AP:74.90**(epoch=160)

    + 01loss1.5 final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001_01loss1.5

      + Recall@1:85.02 Recall@5:90.16 Recall@10:92.01 Recall@top1:98.00 **AP:74.48**(epoch=160)

  

  + drone->satellite 3->1

    + final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001_5

      + **Recall@1:75.93** Recall@5:90.38 Recall@10:93.63 Recall@top1:93.97 **AP:79.20**(epoch=360）
      + Recall@1:75.79 Recall@5:89.98 Recall@10:93.36 Recall@top1:93.72 AP:79.01(epoch=160）

    + 0.5usam  final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001_0.5usam

      + Recall@1:74.66 Recall@5:89.15 Recall@10:92.56 Recall@top1:93.02 AP:77.96(epoch=360）

    + 1usam final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001_usam5

      + Recall@1:75.44 Recall@5:89.69 Recall@10:93.20 Recall@top1:93.56 AP:78.6(epoch=360）

    + 2usam final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001_doubleUsam2

      + Recall@1:73.96 Recall@5:88.99 Recall@10:92.76 Recall@top1:93.22 AP:77.38(epoch=360）

    + SpatialAttention  final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001_SpatialAttention

      + Recall@1:75.45 Recall@5:89.91 Recall@10:93.04 Recall@top1:93.41 AP:78.70(epoch=360）

    + ResSpatialAttention

      final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001_ResSpatialAttention

      + **Recall@1:76.43** Recall@5:90.36 Recall@10:93.69 Recall@top1:94.10 **AP:79.60**(epoch=360）

    + [1,2,3,4,5]CBAM   final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001_5CBAM

      + Recall@1:74.67 Recall@5:88.89 Recall@10:92.28 Recall@top1:92.66 AP:77.90(epoch=160)

    + [1,2,3,4,5]final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001_ResSpatialAttention12345

      + Recall@1:75.06 Recall@5:89.73 Recall@10:93.29 Recall@top1:93.69 AP:78.37(epoch=160)

    + [1,2]final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001_ResSpatialAttention12

      + Recall@1:75.52 Recall@5:89.96 Recall@10:93.41 Recall@top1:93.84 AP:78.77(epoch=160)

    + [CBAM1T]final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001_CBAM1T

      + Recall@1:74.03 Recall@5:88.32 Recall@10:91.99 Recall@top1:92.41 AP:77.25(epoch=160)

    + [CBAM15T]final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001_CBAM15T

      + Recall@1:75.04 Recall@5:89.52 Recall@10:93.03 Recall@top1:93.42 AP:78.28(epoch=160)

    + 01loss1.5 final_three_view_long_share_d0.75_256_s1_google_LPN4_lr0.001_01loss1.5

      + **Recall@1:76.96** Recall@5:90.22 Recall@10:93.26 Recall@top1:93.70 **AP:79.96**(epoch=160)















+ **baseline  （train batchsize=32 epoch=160）**

  + sattlite->drone 1->3 
    +  three_view_long_share_d0.75_256_s1_google_3
      + **Recall@1:71.61** Recall@5:80.31 Recall@10:83.74 Recall@top1:97.00 **AP:58.72**
    + 1usam / three_view_long_share_d0.75_256_s1_google_usam2
      + Recall@1:69.47 Recall@5:79.03 Recall@10:82.17 Recall@top1:97.15 AP:56.43
    + SpatialAttention three_view_long_share_d0.75_256_s1_google_SpatialAttention
      + Recall@1:70.04 Recall@5:78.89 Recall@10:82.03 Recall@top1:97.00 AP:57.00
    + [1]ResSpatialAttention  three_view_long_share_d0.75_256_s1_google_ResSpatialAttention
      + **Recall@1:72.90** Recall@5:81.03 Recall@10:84.31 Recall@top1:97.7**2 AP:58.95**
      + **B Recall@1:74.61** Recall@5:82.17 Recall@10:84.59 Recall@top1:97.43 **AP:61.83**                                                   (batchsize=16)
    + [1]CBAM three_view_long_share_d0.75_256_s1_google_CBAM
      + Recall@1:69.47 Recall@5:77.32 Recall@10:80.74 Recall@top1:96.58 AP:56.54
    + [1,2F]ResSpatialAttention  three_view_long_share_d0.75_256_s1_google_ResSpatialAttention12
      + Recall@1:70.61 Recall@5:78.89 Recall@10:81.88 Recall@top1:96.72 AP:57.14 
    + [1,2T]three_view_long_share_d0.75_256_s1_google_ResSpatialAttention12T
      + Recall@1:70.47 Recall@5:78.89 Recall@10:82.45 Recall@top1:97.00 AP:58.08
    + [1,5]three_view_long_share_d0.75_256_s1_google_ResSpatialAttention15
      + Recall@1:67.48 Recall@5:76.89 Recall@10:79.60 Recall@top1:95.72 AP:53.58
    + ？three_view_long_share_d0.75_256_s1_google_resnetCBAM 
      + Recall@1:19.26 Recall@5:26.39 Recall@10:29.53 Recall@top1:69.33 AP:14.00  (batchsize=16)
    + [CBAM1T]three_view_long_share_d0.75_256_s1_google_CBAM1T
      + **Recall@1:75.32** Recall@5:82.45 Recall@10:84.74 Recall@top1:97.57 **AP:61.78** (batchsize=16)
    + [CBAM15T]three_view_long_share_d0.75_256_s1_google_CBAM15T
      + **Recall@1:75.61** Recall@5:81.03 Recall@10:83.31 Recall@top1:97.43 **AP:60.12** (batchsize=16)
    + [CBAM12T]CBAM three_view_long_share_d0.75_256_s1_google_CBAM12T
      + **Recall@1:74.47** Recall@5:82.17 Recall@10:86.31 Recall@top1:97.57 **AP:61.91**
    + [CBAM11T]CBAM  three_view_long_share_d0.75_256_s1_google_CBAM11T
      + **Recall@1:75.75** Recall@5:82.74 Recall@10:85.59 Recall@top1:97.29 **AP:61.51**

  

  + drone->satellite 3->1 （batchsize=32）
    +  three_view_long_share_d0.75_256_s1_google_3
      + **Recall@1:58.20** Recall@5:79.09 Recall@10:85.44 Recall@top1:86.20 **AP:63.01**
    + 1usam / three_view_long_share_d0.75_256_s1_google_usam2
      + Recall@1:56.20 Recall@5:76.64 Recall@10:83.24 Recall@top1:83.94 AP:60.91
    + SpatialAttention three_view_long_share_d0.75_256_s1_google_SpatialAttention
      + Recall@1:57.94 Recall@5:78.11 Recall@10:84.30 Recall@top1:85.12 AP:62.60
    + [1]ResSpatialAttention  three_view_long_share_d0.75_256_s1_google_ResSpatialAttention
      + **Recall@1:60.15** Recall@5:80.97 Recall@10:87.03 Recall@top1:87.63 **AP:64.86**
      + **B Recall@1:61.13** Recall@5:81.15 Recall@10:86.26 Recall@top1:86.97 **AP:65.70**                                                    (batchsize=16)
    + [1]CBAM three_view_long_share_d0.75_256_s1_google_CBAM
      + Recall@1:56.85 Recall@5:77.16 Recall@10:83.48 Recall@top1:84.33 AP:61.54
    + [1,2F]ResSpatialAttention  three_view_long_share_d0.75_256_s1_google_ResSpatialAttention12
      + **Recall@1:59.00** Recall@5:79.44 Recall@10:85.61 Recall@top1:86.23 **AP:63.65**
    + [1,2T]three_view_long_share_d0.75_256_s1_google_ResSpatialAttention12T
      + Recall@1:57.96 Recall@5:78.99 Recall@10:85.16 Recall@top1:85.88 AP:62.75
    + [1,5]three_view_long_share_d0.75_256_s1_google_ResSpatialAttention15
      + Recall@1:56.02 Recall@5:76.87 Recall@10:83.89 Recall@top1:84.81 AP:60.85
    + ？three_view_long_share_d0.75_256_s1_google_resnetCBAM
      + Recall@1:14.68 Recall@5:28.85 Recall@10:36.73 Recall@top1:37.89 AP:18.47(batchsize=16)
    + [CBAM1T]three_view_long_share_d0.75_256_s1_google_CBAM1T
      + **Recall@1:61.73** Recall@5:81.89 Recall@10:87.40 Recall@top1:88.03 **AP:66.28** (batchsize=16)
    + [CBAM15T]  three_view_long_share_d0.75_256_s1_google_CBAM15T
      + **Recall@1:59.64** Recall@5:80.20 Recall@10:85.52 Recall@top1:86.19 **AP:64.29** (batchsize=16)
    + [CBAM12T]CBAM  three_view_long_share_d0.75_256_s1_google_CBAM12T
      + **Recall@1:62.58** Recall@5:81.56 Recall@10:86.87 Recall@top1:87.62 **AP:66.92**
    + [CBAM11T]CBAM  three_view_long_share_d0.75_256_s1_google_CBAM11T
      + **Recall@1:61.73** Recall@5:80.82 Recall@10:86.41 Recall@top1:87.12 **AP:66.10**

