import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('drawing.jpg')
rows, cols = img.shape[:2]
# 变换前的三个点
pts = np.float32([[50, 65], [150, 65], [210, 210]])
# 变换后的三个点
pts2 = np.float32([[50, 100], [150, 65], [100, 250]])
# 生成变换矩阵
M = cv2.getAffineTransform(pts, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))

plt.subplot(121), plt.imshow(img), plt.title('input')
plt.subplot(122), plt.imshow(dst), plt.title('output')
plt.show()

# 透视变换
img = cv2.imread('card.jpg')
pts1 = np.float32([[148, 80], [437, 114], [94, 247], [423, 288]])
pts2 = np.float32([[0, 0], [320, 0], [0, 178], [320, 178]])

# 生成透视变换矩阵
M = cv2.getPerspectiveTransform(pts1, pts2)
# 进行透视变换，参数3是目标图像大小
dst = cv2.warpPerspective(img, M, (320, 178))
# matplotlib 默认以RGB通道显示，所以需要用[:, :, ::-1] 翻转一下
plt.subplot(121), plt.imshow(img[:, :, ::-1]), plt.title('input')
plt.subplot(122), plt.imshow(dst[:, :, ::-1]), plt.title('output')
plt.show()
