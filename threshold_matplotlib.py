import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Files/Boat.jpg", 0)
img = cv2.resize(img,(600, 400))
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# เปรียบเทียบค่า threshold value ด้วย matplotlib 
thresh_value = [50, 100, 130, 200, 230]
plt.subplot(231, xticks=[], yticks=[])
plt.title("Original")
plt.imshow(img, cmap="gray")
 
for i in range (len(thresh_value)):
    thresh, result = cv2.threshold(img, thresh_value[i], 255, cv2.THRESH_BINARY)
    plt.subplot(232+i)
    plt.title("%d"%thresh_value[i])
    plt.imshow(result, cmap="gray")
    plt.xticks([]),plt.yticks([])

plt.show()