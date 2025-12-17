import cv2

#เปิดวิดีโอ 
video = cv2.VideoCapture("Files/greeting_vid.mp4")

while (video.isOpened()):
    ret, frame = video.read() # เก็บค่า ret (boolean) อ่านได้ = True, อ่านไม่ได้ = False / frame

    if ret == True: # ถ้าวิดีโอยังเล่นไม่จบ ให้แสดงผลออกมา จนกว่ามันจะจบ
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # ทำให้วิดีโอเป็น grayscale
        cv2.imshow("Output", frame) # เปลี่ยนจาก frame เป็น gray ทำให้วิดีโอเป็น grayscale
        if cv2.waitKey(10) & 0xFF == ord("e"): # กดตัว e จะหยุด ออกจากลูป และหยุดทันที
            break
    else: #เมื่อวิดีโอจบจะไม่ค้าง
        break

#เคลียร์ RAM และทรัพยากร
video.release()
cv2.destroyAllWindows()