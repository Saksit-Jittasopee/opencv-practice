import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("Files/CoinNoise.png",0)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# ตัวกรองข้อมุล
kernel1 = np.ones((3,3), np.float32)/9
kernel2 = np.ones((5,5), np.float32)/25

# Convolution
convo1 = cv2.filter2D(img,-1,kernel1)
convo2 = cv2.filter2D(img,-1,kernel2)

# Blur
mean_blur = cv2.blur(img,(5,5))
median_blur = cv2.medianBlur(img,5)
gaussian_blur = cv2.GaussianBlur(img,(5,5),0)

titles = ["ORIGINAL", "CONVOLUTION 3X3", "CONVOLUTION 5X5", "MEAN FILTERING", "MEDIAN FILTERING", "GAUSSIAN FILTERING"]
images = [img, convo1, convo2, mean_blur, median_blur, gaussian_blur]

for i in range (len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()