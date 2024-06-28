import cv2

img = cv2.imread(r'D:\SmartCoding\opencv\img.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite(r'D:\SmartCoding\opencv\out.jpg', gray)