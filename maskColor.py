import cv2
import numpy as np

while True:
    img = cv2.imread("Files/ColorBalls.webp", 1)
    img = cv2.resize(img,(400, 400))

    #green
    # upper = np.array([96, 255, 123])
    # lower = np.array([7, 105, 10])

    #blue
    upper = np.array([255, 231, 136])
    lower = np.array([161, 50, 2])

    mask = cv2.inRange(img, lower, upper) # mask สีจากช่วงสีที่กำหนด
    result = cv2.bitwise_and(img, img, mask=mask) # แทนที่สีขาวที่ mask ด้วยสี

    if cv2.waitKey(10) & 0xFF == ord("e"): # กดตัว e จะหยุด ออกจากลูป และหยุดทันที
        break
    cv2.imshow("Output", img)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result) 
    

cv2.waitKey(0)
cv2.destroyAllWindows()
