import cv2

img = cv2.imread('./assets/solar-system.jpg')
cv2.putText(img, 'Sun', (20, 300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, 'Mercury', (110, 190), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, 'Venus', (190, 260), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, 'Earth', (290, 260), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, 'Mars', (380, 260), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, 'Jupiter', (480, 80), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, 'Saturn', (700, 260), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, 'Uranus', (965, 285), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, 'Neptune', (1110, 285), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.imwrite('./assets/Solar_systemwithname.jpg', img)