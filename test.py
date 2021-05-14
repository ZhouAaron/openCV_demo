# import cv2
#
# img = cv2.imread('./imageFile/drawing.jpg')
# res = cv2.resize(img,(132,150))
# res2 = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_LINEAR)
#
#
# cv2.imshow('shrink',res), cv2.imshow('zoom1',res2)
# cv2.waitKey(0)

import cv2
capture = cv2.VideoCapture(0)
while(True):
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) == ord('q'):
        break