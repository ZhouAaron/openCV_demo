import cv2
import matplotlib.image as pli
import matplotlib.pyplot as plt
# 1.显示灰度图
img = cv2.imread('lena.jpg', 0)
plt.imshow(img, cmap='gray')
plt.show()

# 2.显示彩色图
img = cv2.imread('lena.jpg')
# img[:, :, :0] 表示图片的蓝色通道， img[:, :, ::-1]表示bgr 翻转 变成rgb
# 对于字符串 s[::-1] 可以表示翻转
img2 = img[:, :, ::-1]
# 显示不正确的图
plt.subplot(121), plt.imshow(img)
# 显示正确的图
plt.subplot(122)
plt.xticks([]), plt.yticks([])
plt.show()
# 加载和保存图片
img = pli.imread('lena.jpg')
plt.imshow(img)
# 保存图片
plt.savefig('lena2.jpg')
plt.show()

