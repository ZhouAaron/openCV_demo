import  cv2
import matplotlib.pyplot as plt

img = cv2.imread('./image/sudoku.jpg', 0)
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# 小区域内取均值 11 就是11*11 的小块
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 4)
# 小区域内加权求和，权重是高斯核
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 6)
titles = ['Original', 'Global(V = 127)', 'Adaptive Mean', 'Adaptive Gaussain']
images = [img, th1, th2, th3]
for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i], fontsize=8)
    plt.xticks([]), plt.yticks([])
plt.show()