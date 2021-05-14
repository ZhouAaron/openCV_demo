import cv2
import matplotlib.pyplot as plt

img = cv2.imread("./image/gradient.jpg",0)
ret,th = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow('thresh',th)
cv2.waitKey(0)
