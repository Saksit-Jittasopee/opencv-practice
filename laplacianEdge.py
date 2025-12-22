import cv2

img = cv2.imread("Files/CoinNoise.png",0)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img = cv2.resize(img,(600, 400))

laplacian = cv2.Laplacian(img, -1)

cv2.imshow("Original", img)
cv2.imshow("Laplacian", laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()