import cv2
import numpy as np
# 1.图片相加
x = np.uint8([250])
y = np.uint8([10])
print(cv2.add(x, y))
print(x + y)
# 2.图像混合
#
img1 = cv2.imread('./imageFile/lena_small.jpg')
img2 = cv2.imread('./imageFile/opencv-logo-white.png')
res = cv2.addWeighted(img1, .6, img2, .4, 0)
cv2.imshow('blending', res)
rows, cols = img2.shape[:2]
roi = img1[:rows, :cols]
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
# 保留除log外的背景
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
dst = cv2.add(img1_bg, img2)
img1[:rows, :cols] = dst
cv2.imshow('result', img1)
cv2.waitKey(0)
