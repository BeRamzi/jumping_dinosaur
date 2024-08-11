import numpy as np
import cv2

i=0
while True:

    canvas_window = cv2.namedWindow('dinosaur', cv2.WINDOW_AUTOSIZE)
    image = np.load("array" + str(i)+".npy")
    width, height = image.shape
    canvas = np.zeros((int(width),int(height/10)+7))
    image_copy = image.copy()
    image_copy[:20,:height]= 0

    image_copy[:int(width),:int(height/10)+7]= 0
    kernel = np.ones((4,4), np.uint8)
    eroded = cv2.erode(image_copy,kernel, iterations=1)
    dilated = cv2.dilate(eroded,kernel, iterations=2)
    contours,_ = cv2.findContours(dilated,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(image, contours, -1, (50, 209, 255), 1)
    min_area = 40  # Minimum contour area
    max_area = 3000  # Maximum contour area
    image = cv2.cvtColor(dilated,cv2.COLOR_GRAY2RGB)

    # Filter contours based on area
    filtered_contours = [cnt for cnt in contours if min_area <= cv2.contourArea(cnt) <= max_area]

    for contour in filtered_contours:
        # Get the bounding rectangle for the contour
        x, y, w, h = cv2.boundingRect(contour)
        # Draw the rectangle on the original image
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255,0 ), 2)
    cv2.imshow('dinosaur',image)
    key = cv2.waitKey(15) & 0xFF
    if key == ord('q'):
        break
    i+=1
    if i == 10000:
        break

cv2.destroyAllWindows()


# image = np.load("array4000.npy")
# width, height = image.shape
# canvas = np.zeros((int(width),int(height/10)))
# image_copy = image.copy()
# image_copy[:24,:height]= 0
# image_copy[:int(width),:int(height/10)]= 0
# kernel = np.ones((4,4), np.uint8)
# eroded = cv2.erode(image_copy,kernel, iterations=1)
# dilated = cv2.dilate(eroded,kernel, iterations=2)
# contours , _ = cv2.findContours(dilated,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# print(len(contours))
# min_area = 40  # Minimum contour area
# max_area = 3000  # Maximum contour area
# image = cv2.cvtColor(dilated,cv2.COLOR_GRAY2RGB)

# # Filter contours based on area
# filtered_contours = [cnt for cnt in contours if min_area <= cv2.contourArea(cnt) <= max_area]

# for contour in filtered_contours:
#     # Get the bounding rectangle for the contour
#     x, y, w, h = cv2.boundingRect(contour)
#     # Draw the rectangle on the original image
#     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 23), 2)
# cv2.drawContours(image, contours, -1, (0, 0, 255), 1)
# cv2.imshow('dinosaur',image)
# key = cv2.waitKey(0) & 0xFF
# if key == ord('q'):
#     cv2.destroyAllWindows()


