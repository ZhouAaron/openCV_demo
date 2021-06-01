import cv2
import numpy as np
# 1. 腐蚀与膨胀
img = cv2.imread('j.bmp', 0)
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel)  # 腐蚀
dilation = cv2.dilate(img, kernel)  # 膨胀

cv2.imshow('erosion/dilation', np.hstack((img, erosion, dilation)))
cv2.waitKey(0)

# 定义结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # 矩形结构
print(kernel)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))  # 椭圆结构ellipse
print(kernel)
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))  # 十字架结构
print(kernel)

# 开运算和闭运算
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# 开运算
img = cv2.imread('j_noise_out.bmp', 0)
# 闭运算
img = cv2.imread('j_noise_in.bmp', 0)
closeing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow('closing', np.hstack((img, closeing)))
cv2.waitKey(0)

# 形态学梯度
img = cv2.imread('school.bmp', 0)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('morphological gradient', np.hstack((img, gradient)))
cv2.waitKey(0)

# 顶帽
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow('top hat', np.hstack((img, tophat)))
cv2.waitKey(0)

# 黑帽
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow('black hat', np.hstack((img, blackhat)))
cv2.waitKey(0)