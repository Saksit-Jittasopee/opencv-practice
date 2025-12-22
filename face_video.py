import cv2

cap = cv2.VideoCapture("Files/Boom.mp4")

# อ่านไฟล์สำหรับ classification
face_cascade = cv2.CascadeClassifier("Detect/haarcascade_frontalface_default.xml")
#eye_cascade = cv2.CascadeClassifier("Detect/haarcascade_eye_tree_eyeglasses.xml")

# แสดงผลวิดีโอ
while (cap.isOpened()):
    check, frame = cap.read()
    if check == True:
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # จำแนกใบหน้า
        scaleFactor = 1.1 # Default
        minNeighbors = 3 # Default
        face_detect = face_cascade.detectMultiScale(gray_img, scaleFactor, minNeighbors)
        #eye_detect = eye_cascade.detectMultiScale(gray_img, scaleFactor, minNeighbors)
        # แสดงตำแหน่งที่เจอใบหน้า
        for (x,y,w,h) in face_detect: #เปลี่ยนเป็น eye_detect เพื่อจับดวงตา
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=5)
            cv2.imshow("Output", frame)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()