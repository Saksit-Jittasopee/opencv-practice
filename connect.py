import cv2
import numpy as np
img = np.zeros([400,400,3])
points = []

def clickPostion(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(0,0,255),5)
        points.append((x,y)) #เก็บค่าพิกัดที่คลิ๊ก
        if len(points) >= 2:
            cv2.line(img, points[-2], points[-1], (0,255,0), 5)
        cv2.imshow("Output", img)

cv2.imshow("Output", img)
cv2.setMouseCallback("Output",clickPostion)
cv2.waitKey(0)
cv2.destroyAllWindows()