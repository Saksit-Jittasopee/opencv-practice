import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Files/Boat.jpg", 0)
img = cv2.resize(img,(600, 400))
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
thresh, result1 = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
thresh, result2 = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
thresh, result3 = cv2.threshold(img, 128, 255, cv2.THRESH_TRUNC)
thresh, result4 = cv2.threshold(img, 128, 255, cv2.THRESH_TOZERO)
thresh, result5 = cv2.threshold(img, 128, 255, cv2.THRESH_TOZERO_INV)

# cv2.imshow("Original", img)
# cv2.imshow("Binary", result1)
#cv2.imshow("Binary Invert", result2)
#cv2.imshow("Trunc", result3)
#cv2.imshow("To Zero", result4)
#cv2.imshow("To Zero Invert", result5)

# แสดงใน matplotlib 
images = [img, result1, result2, result3, result4, result5]
titles = ["Original", "Binary", "Binary Invert", "Trunc", "To Zero", "To Zero Invert"]

for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
plt.show()

# cv2.waitKey(0)
# cv2.destroyAllWindows()
