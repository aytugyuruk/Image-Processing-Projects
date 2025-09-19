import cv2
import numpy as np

mm = cv2.imread("mm.jpg")
mm_hsv = cv2.cvtColor(mm, cv2.COLOR_BGR2HSV)

#===========================================================
# Mavi renk aralığı
blue_lower = np.array([100, 120, 50])
blue_upper = np.array([130, 255, 255])
mask_blue = cv2.inRange(mm_hsv, blue_lower, blue_upper)

# Kırmızı (iki aralık gerekiyor HSV’de kırmızı uçta olduğu için)
red_lower1 = np.array([0, 100, 100])
red_upper1 = np.array([10, 255, 255])
red_lower2 = np.array([160, 100, 100])
red_upper2 = np.array([179, 255, 255])
mask_red1 = cv2.inRange(mm_hsv, red_lower1, red_upper1)
mask_red2 = cv2.inRange(mm_hsv, red_lower2, red_upper2)
mask_red = cv2.bitwise_or(mask_red1, mask_red2)

# Turuncu
orange_lower = np.array([10, 100, 100])
orange_upper = np.array([25, 255, 255])
mask_orange = cv2.inRange(mm_hsv, orange_lower, orange_upper)

# Sarı
yellow_lower = np.array([25, 100, 100])
yellow_upper = np.array([35, 255, 255])
mask_yellow = cv2.inRange(mm_hsv, yellow_lower, yellow_upper)

# Yeşil
green_lower = np.array([35, 80, 80])   # Açık yeşilden başlaması için hue’yu düşürdük
green_upper = np.array([85, 255, 255]) # Koyu yeşile uzatmak için hue’yu genişlettik
mask_green = cv2.inRange(mm_hsv, green_lower, green_upper)
#===========================================================
template = cv2.imread("template.jpg")
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
_, template = cv2.threshold(template, 240, 255, cv2.THRESH_BINARY)
contours_template, _ = cv2.findContours(template, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
sum_template_area = 0
for cnt in contours_template:
    area = cv2.contourArea(cnt)
    if area > 10000:
       sum_template_area += area
#===========================================================
contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
blue_count = 0
for cnt in contours_blue:
    area = cv2.contourArea(cnt)
    if area > 10000:
       cv2.drawContours(mm, [cnt], -1, (255,0,0), 5)
       if area > sum_template_area*0.8 and area < sum_template_area*1.5:
            blue_count += 1
       elif area > sum_template_area*1.5 and area < sum_template_area*2.5:
            blue_count += 2
       elif area > sum_template_area*2.5 and area < sum_template_area*3.5:
            blue_count += 3
       elif area > sum_template_area*3.5 and area < sum_template_area*4.5:
            blue_count += 4
       elif area > sum_template_area*4.5 and area < sum_template_area*5.5:
            blue_count += 5
print(f"Blue objects: {blue_count}")
#===========================================================
contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
red_count = 0
for cnt in contours_red:
    area = cv2.contourArea(cnt)
    if area > 10000:
       cv2.drawContours(mm, [cnt], -1, (0,0,255), 5)
       if area > sum_template_area*0.8 and area < sum_template_area*1.5:
            red_count += 1
       elif area > sum_template_area*1.5 and area < sum_template_area*2.5:
            red_count += 2
       elif area > sum_template_area*2.5 and area < sum_template_area*3.5:
            red_count += 3
       elif area > sum_template_area*3.5 and area < sum_template_area*4.5:
            red_count += 4
       elif area > sum_template_area*4.5 and area < sum_template_area*5.5:
            red_count += 5
print(f"Red objects: {red_count}")
#===========================================================
contours_orange, _ = cv2.findContours(mask_orange, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
orange_count = 0
for cnt in contours_orange:
    area = cv2.contourArea(cnt)
    if area > 10000:
       cv2.drawContours(mm, [cnt], -1, (0,140,255), 5)
       if area > sum_template_area*0.8 and area < sum_template_area*1.5:
            orange_count += 1
       elif area > sum_template_area*1.5 and area < sum_template_area*2.5:
            orange_count += 2
       elif area > sum_template_area*2.5 and area < sum_template_area*3.5:
            orange_count += 3
       elif area > sum_template_area*3.5 and area < sum_template_area*4.5:
            orange_count += 4
       elif area > sum_template_area*4.5 and area < sum_template_area*5.5:
            orange_count += 5
print(f"Orange objects: {orange_count}")
#===========================================================
contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
yellow_count = 0
for cnt in contours_yellow:
    area = cv2.contourArea(cnt)
    if area > 10000:
       cv2.drawContours(mm, [cnt], -1, (0,255,255), 5)
       if area > sum_template_area*0.8 and area < sum_template_area*1.5:
            yellow_count += 1
       elif area > sum_template_area*1.5 and area < sum_template_area*2.5:
            yellow_count += 2
       elif area > sum_template_area*2.5 and area < sum_template_area*3.5:
            yellow_count += 3
       elif area > sum_template_area*3.5 and area < sum_template_area*4.5:
            yellow_count += 4
       elif area > sum_template_area*4.5 and area < sum_template_area*5.5:
            yellow_count += 5
print(f"Yellow objects: {yellow_count}")
#===========================================================
contours_green, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
green_count = 0
for cnt in contours_green:
    area = cv2.contourArea(cnt)
    if area > 10000:
       cv2.drawContours(mm, [cnt], -1, (0,255,0), 5)
       if area > sum_template_area*0.8 and area < sum_template_area*1.5:
            green_count += 1
       elif area > sum_template_area*1.5 and area < sum_template_area*2.5:
            green_count += 2
       elif area > sum_template_area*2.5 and area < sum_template_area*3.5:
            green_count += 3
       elif area > sum_template_area*3.5 and area < sum_template_area*4.5:
            green_count += 4
       elif area > sum_template_area*4.5 and area < sum_template_area*5.5:
            green_count += 5
print(f"Green objects: {green_count}")
#===========================================================
cv2.putText(mm, f"Blue: {blue_count}", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
cv2.putText(mm, f"Red: {red_count}", (10,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
cv2.putText(mm, f"Orange: {orange_count}", (10,110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,140,255), 2)
cv2.putText(mm, f"Yellow: {yellow_count}", (10,150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
cv2.putText(mm, f"Green: {green_count}", (10,190), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
#===========================================================
cv2.imshow("img", mm)
cv2.imwrite("result.jpg", mm)
cv2.waitKey(0)
cv2.destroyAllWindows()