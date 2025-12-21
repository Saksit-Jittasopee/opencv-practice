#อ่านภาพ
import cv2

# 0 - grayscale, 1 - color, -1 - alpha
img = cv2.imread("Files/Saksit_2.jpg", 1)
#Resize ภาพ
img_resize = cv2.resize(img,(600, 400))

#แสดงพิกัดเวลาคลิ๊กที่ภาพ
def clickPostion(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img_resize[y,x,0] #detect color blue
        green = img_resize[y,x,1] #detect color green
        red = img_resize[y,x,2] #detect color red
        #text = str(x)+","+str(y) #แสดงตำแหน่งพิกัด
        color = str(blue)+","+str(green)+","+str(red) #แสดงการตรวจจับสี
        cv2.putText(img_resize, color, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), cv2.LINE_4)
        cv2.imshow("Output", img_resize)

#Show 3D Array
#print(img_resize)

#แสดงผลภาพ (Title, Variable)
cv2.imshow("Output", img_resize)

#ทำงานกับ mouse
cv2.setMouseCallback("Output",clickPostion)

#สร้าง/เขียนไฟล์ใหม่
# cv2.imwrite("Saksit-New.jpg", img_resize)

#เวลาที่แสดงเป็น ms ก่อนจะปิด
cv2.waitKey(0)
#cv2.waitKey(delay=5000)
cv2.destroyAllWindows()