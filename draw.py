import cv2

# 0 - grayscale, 1 - color, -1 - alpha
img = cv2.imread("Files/Saksit_2.jpg", 1)
#Resize ภาพ
img_resize = cv2.resize(img,(600, 400))
#Show 3D Array
print(img_resize)

#วาดเส้นตรง (ภาพ, จุดเริ่มต้น, จุดสุดท้าย, สี(B,G,R), ความหนา)
#cv2.line(img_resize,(100,100),(200,220),(0,255,0),5) ไม่มีลูกศร
cv2.arrowedLine(img_resize,(100,100),(200,220),(0,255,0),5)

#วาดสี่เหลี่ยม (ภาพ, มุม 1 บนซ้าย, มุม 2 ล่างขวา, สี(B,G,R), ความหนา (-1 คือ fill)) 
cv2.rectangle(img_resize,(10,10),(400,300),(255,0,0),1)

#วาดวงกลม (ภาพ, จุดศูนย์กลาง, รัศมี, สี(B,G,R), ความหนา (-1 คือ fill)) 
cv2.circle(img_resize,(400,270),30,(0,0,255),10)

#วาดข้อความ (ภาพ, ข้อความ, ตำแหน่ง, font, ขนาด, สี(B,G,R), ความหนา)
cv2.putText(img_resize, "I met Zack", (150,250), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255))

#แสดงผลภาพ (Title, Variable)
cv2.imshow("Output", img_resize)

#สร้าง/เขียนไฟล์ใหม่
# cv2.imwrite("Saksit-New.jpg", img_resize)

#เวลาที่แสดงเป็น ms ก่อนจะปิด
cv2.waitKey(0)
cv2.destroyAllWindows()