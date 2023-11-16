import cv2
path = "C:/Users/P Leela Mohan/Pictures/raju ooty tour/20181027_094216.jpg"
src = cv2.imread(path)
window_name = 'Image'
image = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow(window_name, image)
cv2.waitKey(0) 
