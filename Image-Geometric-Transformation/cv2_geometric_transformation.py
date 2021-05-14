# 实现旋转、平移和缩放图片
import cv2
import numpy as np
img = cv2.imread('drawing.jpg')
res = cv2.resize(img, (132,150))
res2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

cv2.imshow('shrink', res), cv2.imshow('zoom',res2)

# 2. 翻转图片
# 参数2=0 垂直翻转（沿X轴），参数2>0:水平翻转（沿y轴）
#参数2<0：水平垂直翻转
dst = cv2.flip(img,-1)
cv2.imshow('flip', np.hstack((img, dst))) # 横向并排，对比显示


# 3. 平移图片
rows, cols = img.shape[:2]
#定义平移矩阵，需要是numpy的float32类型
#x轴平移100，y轴平移50
M = np.float32([[1, 0, 100], [0, 1, 50]])

dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('shift', dst)


#4 . 45 顺时针旋转图片并缩小一半
M = cv2.getRotationMatrix2D((cols / 20, rows / 2), -45,0.5)
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('rotation', dst)
cv2.waitKey(0)
