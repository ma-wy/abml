#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *
 

def line_direct_filter(degree, degree_delta, mask):
    # 添加padding 保护图片在旋转时边缘像素的丢失，保证旋转后的图片大小不变，且旋转后的图片中心与原图中心重合，方便后续处理
    circumcircle_diameter = int(math.sqrt(mask.shape[0] ** 2 + mask.shape[1] ** 2))  # 计算外接圆直径，即旋转后的图片大小
    circumcircle_radius = circumcircle_diameter // 2  # 计算外接圆半径
    width_pad = (circumcircle_diameter - mask.shape[0]) // 2  # 计算padding的宽度
    height_pad = (circumcircle_diameter - mask.shape[1]) // 2  # 计算padding的高度
    mask_with_pad = np.pad(mask, ((width_pad, width_pad), (height_pad, height_pad)), 'constant',
                           constant_values=0)  # 添加padding
    r_src = np.zeros_like(mask_with_pad)  # 用于提取线条的空白图像
    for deg in range(degree - degree_delta, degree + degree_delta, 1):  # 旋转角度+可容忍的误差合成一个范围
        horizon_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (mask.shape[1] // 32, 1), (-1, -1))  # 水平方向的kernel
        affine_mat = cv2.getRotationMatrix2D((circumcircle_radius, circumcircle_radius), deg, 1)  # 旋转矩阵
        _mask = cv2.warpAffine(mask_with_pad, affine_mat, (circumcircle_diameter, circumcircle_diameter))  # 旋转图片
        _r_src = cv2.warpAffine(r_src, affine_mat, (circumcircle_diameter, circumcircle_diameter))  # 旋转空白图像，方便后续合成最终的目标
        _r_src = cv2.morphologyEx(_mask, cv2.MORPH_OPEN, horizon_kernel)  # 提取水平线条
        
img = cv2.imread('/home/abml/zoe_data/gs.png')
img = cv2.Canny(img, 50, 150, apertureSize=3)
img = line_direct_filter(0, 5, img)        
cv2.imshow('Original', img)
cv2.waitKey(0)
'''
# Display original image
cv2.imshow('Original', img)
cv2.waitKey(0)

# Convert to graycsale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 

# Sobel Edge Detection
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
# Display Sobel Edge Detection Images
cv2.imshow('Sobel X', sobelx)
cv2.waitKey(0)
cv2.imshow('Sobel Y', sobely)
cv2.waitKey(0)
cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
cv2.waitKey(0)

# Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
# Display Canny Edge Detection Image
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)

cv2.destroyAllWindows()
'''









    
