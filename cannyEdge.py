import cv2

img = cv2.imread("Files/CoinNoise.png",0)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img = cv2.resize(img,(600, 400))

canny = cv2.Canny(img, 50, 200)

cv2.imshow("Original", img)
cv2.imshow("Canny", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()