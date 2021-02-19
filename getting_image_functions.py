import numpy as np
import cv2

# how to read an image
img = cv2.imread('Rosie.JPG', 0)
height, width = img.shape[:2]
# img = cv2.line(img, (0, 0), (255, 255), (144, 96, 44), 10)
# img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 10)

img = cv2.rectangle(img, (100, 100), (350, 250), (255, 0, 0), 10)
# img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, 'Rosie Picture', (100, 400), font, 4, (255, 255, 255), 10, cv2.LINE_AA)
cv2.imshow('Test', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
