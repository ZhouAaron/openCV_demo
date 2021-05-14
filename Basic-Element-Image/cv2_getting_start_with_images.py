import cv2
img = cv2.imread('../imageFile/lena.jpg')
px = img[100,90]
print(px)
px_blue = img[100,90,0]
print(px_blue)
print(img.shape)
height, width, channels = img.shape
print(img.dtype)
print(img.size)
face = img[100:200,115:188]
cv2.imshow('face',face)
cv2.waitKey(0)
b, g, r = cv2.split(img)
img = cv2.merge(b,g,r)
