import cv2

#ระบุเลขกล้อง - กล้องตัวเดียว 0 / กล้องสองตัว 0,1
webcam = cv2.VideoCapture(0)

while (True):
    ret, frame = webcam.read() # เก็บค่า ret (boolean) อ่านได้ = True, อ่านไม่ได้ = False / frame
    cv2.imshow("Output", frame)

    if cv2.waitKey(1) & 0xFF == ord("e"): # กดตัว e จะหยุด ออกจากลูป และปิดกล้อง
        break

#เคลียร์ RAM และทรัพยากร
webcam.release()
cv2.destroyAllWindows()
