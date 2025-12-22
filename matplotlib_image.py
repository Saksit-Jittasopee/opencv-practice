import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Files/Saksit_1.jpg")
cv2.imshow("Output", img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# เปลี่ยนเป็นสี RGB
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.show()