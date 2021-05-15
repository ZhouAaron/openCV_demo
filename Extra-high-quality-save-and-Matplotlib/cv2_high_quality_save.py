import cv2
import numpy as  np
new_img = cv2.imread('lena.jpg')
 # bmp
cv2.imwrite('img_bmp.bmp', new_img)
# jpg 默认95%的质量
cv2.imwrite('img_jpg95.jpg', new_img)
# jpg 20%的质量
cv2.imwrite('img_jpg20.jpg', new_img, [
    int(cv2.IMWRITE_JPEG_QUALITY), 20])
# jpg 100%的质量
cv2.imwrite('img_jpg100.jpg', new_img, [
    int(cv2.IMWRITE_JPEG_QUALITY), 100])
# png 默认1压缩比
cv2.imwrite('img_png1.png', new_img)
# png 默认9压缩比
cv2.imwrite('img_png9.png', new_img, [
    int(cv2.IMWRITE_PNG_COMPRESSION), 9])
