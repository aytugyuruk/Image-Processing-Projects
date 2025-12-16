import cv2 
import numpy as np
from matplotlib import pyplot as plt
from rembg import remove


img = cv2.imread("image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
removed = remove(img)
edges = cv2.Canny(removed, 50, 150)
edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, np.ones((5,5), np.uint8))

contours = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
biggest = max(contours, key=cv2.contourArea)

hull = cv2.convexHull(biggest)
epsilon = 0.02 * cv2.arcLength(hull, True)
approx = cv2.approxPolyDP(hull, epsilon, True)

points = approx.reshape((4, 2))
points = sorted(points, key=lambda x: x[0])


# NOKTALARIN KONUMLARINI BULMA
if points[0][1] < points[1][1]:
    leftup = points[0]
    leftdown = points[1]
else:
    leftup = points[1]
    leftdown = points[0]

if points[2][1] < points[3][1]:
    rightup = points[2]
    rightdown = points[3]
else:
    rightup = points[3]
    rightdown = points[2]

x_length = max(np.linalg.norm(rightup - leftup), np.linalg.norm(rightdown - leftdown))
y_length = max(np.linalg.norm(rightup - rightdown), np.linalg.norm(leftup - leftdown))

# ===================================

pts1 = np.array([leftup, rightup, rightdown, leftdown], dtype="float32")
pts2 = np.array([[0,0], [x_length-1,0], [x_length-1,y_length-1], [0,y_length-1]], dtype="float32")

M = cv2.getPerspectiveTransform(pts1, pts2)
warped = cv2.warpPerspective(img, M, (int(x_length), int(y_length)))

#===================================
# Grayscale'e çevir (zaten grayscale ise bu adımı atlayabilirsiniz)
gray = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)

# Piksel değeri 125'in üzerinde olanları beyaz, altındakileri siyah yap
_, binary = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)

binary = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
#====================================



cv2.imwrite("scanned_adjusted.jpg", binary)
cv2.imwrite("scanned.jpg", warped)

plt.subplot(1,3,1)
plt.imshow(img)
plt.subplot(1,3,2)
plt.imshow(warped)
plt.subplot(1,3,3)
plt.imshow(binary)
plt.show()