import cv2

img = cv2.imread("Files/map.jpg", 0)
thresh, th1 = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
# Blocksize เปลี่ยนจาก 3 เป็นเลขอื่นได้ เวลาเพิ่ม ความคมชัดก็จะเพิ่มมากขึ้น
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,1)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,1)

cv2.imshow("THRESH", th1)
cv2.imshow("MEAN", th2)
cv2.imshow("GAUSSIAN", th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
