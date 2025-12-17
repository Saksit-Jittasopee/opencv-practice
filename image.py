#อ่านภาพ
import cv2

# 0 - grayscale, 1 - color, -1 - alpha
img = cv2.imread("Files/Saksit_2.jpg", 1)
#Resize ภาพ
img_resize = cv2.resize(img,(600, 400))
#Show 3D Array
print(img_resize)

#แสดงผลภาพ (Title, Variable)
cv2.imshow("Output", img_resize)

#สร้าง/เขียนไฟล์ใหม่
# cv2.imwrite("Saksit-New.jpg", img_resize)

#เวลาที่แสดงเป็น ms ก่อนจะปิด
cv2.waitKey(delay=5000)
cv2.destroyAllWindows()