import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Files/CoinNoise.png",0)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

sobelX = cv2.Sobel(img, -1, 1, 0)
sobelY = cv2.Sobel(img, -1, 0, 1)
sobelXY = cv2.bitwise_or(sobelX,sobelY)

images = [img, sobelX, sobelY, sobelXY]
titles = ["ORIGINAL", "SOBEL X", "SOBEL Y", "SOBEL XY"]

for i in range (len(images)):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()