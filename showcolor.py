import cv2
import numpy as np

img = cv2.imread("Files/RGB.png", 1)

#แสดงพิกัดเวลาคลิ๊กที่ภาพ
def clickPostion(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x,0] #detect color blue
        green = img[y,x,1] #detect color green
        red = img[y,x,2] #detect color red
        imgcolor = np.zeros([300,300,3],np.uint8) #แสดงค่าสีที่อ่านได้ 8 ตัว
        imgcolor[:] = [blue,green,red] # อิงจาก BGR
        color = str(blue)+","+str(green)+","+str(red) #แสดงการตรวจจับสี
        cv2.putText(img, color, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), cv2.LINE_4)
        cv2.imshow("Result", imgcolor) #หน้าต่างใหม่

cv2.imshow("Output", img)
cv2.setMouseCallback("Output",clickPostion)
cv2.waitKey(0)
cv2.destroyAllWindows()