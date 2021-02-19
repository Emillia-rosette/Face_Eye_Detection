import cv2
# how to read an image
img = cv2.imread('Rosie.JPG', -1)

cv2.imshow('image', img)
k = cv2.waitKey(5000) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('Rosie_copy.png', img)
    cv2.destroyAllWindows()


