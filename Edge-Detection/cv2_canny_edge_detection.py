import cv2
import numpy as np

# 边缘检测本身属于锐化操作，对噪点比较敏感，所以需要进行平滑处理
img = cv2.imread('handwriting.jpg', 0)
edges = cv2.Canny(img, 30, 70)  # canny边缘检测
# canny() 参数2，3表示最低最高阈值
cv2.imshow('canny', np.hstack((img, edges)))
cv2.waitKey(0)
#todo(aaron)
# 1. 使用5*5高斯滤波消除噪声
# 2. 计算图像梯度的方向
# 3. 取局部最大值
# 4. 滞后阈值

# 先阈值，后边缘检测
# 阈值分割（使用到了番外篇讲到的Otsu自动阈值
thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
edges = cv2.Canny(thresh, 30 ,70)
cv2.imshow('canny', np.hstack((img, thresh, edges)))
cv2.waitKey(0)