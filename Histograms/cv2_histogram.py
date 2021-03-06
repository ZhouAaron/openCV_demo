import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('hist.jpg', 0)

# 1. 直方图计算
# 使用OpenCV函数计算
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# 使用numpy函数计算 ravel函数将二维矩阵展平变成一维数组
hist, bins = np.histogram(img.ravel(), 256, [0, 256])

# 使用numpy函数计算
hist = np.bincount(img.ravel(), minlength=256)

# 2. 绘制直方图
plt.hist(img.ravel(), 256, [0, 256])
plt.show()

# 或使用前面计算的直方图结果
plt.plot(hist)
plt.show()

# 3.直方图均衡化
equ = cv2.equalizeHist(img)
cv2.imshow('eaualization', np.hstack((img, equ)))
cv2.waitKey(0)

# 绘制均衡化后的直方图
plt.hist(equ.ravel(), 256, [0, 256])
plt.show()

# 4. 自适应直方图均衡化
img = cv2.imread('tsukuba.jpg', 0)
equ = cv2.equalizeHist(img)
# 自适应均衡化， 参数可选
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img)

cv2.imshow('equalization', np.hstack((equ, equ, cl1)))  # 并排显示
