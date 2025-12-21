import cv2

img = cv2.imread("Files/Saksit_AI_Days_1.jpg", 1)

# อ่านไฟล์สำหรับ classification
face_cascade = cv2.CascadeClassifier("Detect/haarcascade_frontalface_default.xml")

# แปลงให้เป็น grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# จำแนกใบหน้า
scaleFactor = 1.1 # Default
minNeighbors = 3 # Default
face_detect = face_cascade.detectMultiScale(gray_img, scaleFactor, minNeighbors)

# แสดงตำแหน่งที่เจอใบหน้า
for (x,y,w,h) in face_detect:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=5)

cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()