import keyboard
import time
from PIL import ImageGrab, Image
import numpy as np
import cv2
from selenium import webdriver
import base64
from io import BytesIO
from selenium.webdriver.common.by import By

WINDOW_NAME = 'dinosaur'

driver = webdriver.Chrome()
driver.get('https://dino-chrome.com/')
canvas_class_name = 'runner-canvas'  # Replace with the actual class name
canvas = driver.find_element(By.CLASS_NAME, canvas_class_name)
while_break = False

canvas_window = cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_AUTOSIZE)

    # Time delay between key press events
key_press_delay = 0.2  # in seconds
last_key_press_time = time.time()

def on_spacebar_press(event):
    global spacebar_pressed, x_positions, y_positions, x_min, y_min, last_key_press_time
    current_time = time.time()
    if current_time - last_key_press_time >= key_press_delay:
        if not spacebar_pressed:
            spacebar_pressed = True
            last_key_press_time = current_time
            if x_min is not None and y_min is not None:
                x_positions.append(x_min)
                y_positions.append(y_min)
                print(f"Spacebar pressed, stored position: ({x_min}, {y_min})")

def on_spacebar_release(event):
    global spacebar_pressed
    spacebar_pressed = False

# Register the spacebar key press and release events
keyboard.on_press_key("space", on_spacebar_press)
keyboard.on_release_key("space", on_spacebar_release)

# Execute JavaScript to get the canvas data URL
# canvas_data_url = driver.execute_script("""
#     var canvas = document.getElementsByClassName('runner-canvas')[0];
#     return canvas.toDataURL('image/png');
# """)



# Decode the base64 data URL to get the image data
# image_data = base64.b64decode(canvas_data_url.split(',')[1])
# image = Image.open(BytesIO(image_data))

# # Convert the PIL Image to a numpy array
# image_array = np.array(image)
# red_channel = image_array[:, :, 0]

# cv2.imshow('red',red_channel )
# cv2.waitKey(0)
# cv2.destroyWindow('red')
# green_channel = image_array[:, :, 1]
# cv2.imshow('green',green_channel )
# cv2.waitKey(0)
# cv2.destroyWindow('green')
# blue_channel = image_array[:, :, 2]
# cv2.imshow('blue',blue_channel )
# cv2.waitKey(0)
# cv2.destroyWindow('blue')
    
# alpha_channel = image_array[:, :, 3]
# cv2.imshow('alpha',alpha_channel )
# cv2.waitKey(0)
# cv2.destroyWindow('alpha')
 # Register the spacebar key press event



# i=0
# x_positions= list()
# y_positions = list()
# spacebar_pressed = False
# while True:
#     if while_break:
#         break
    
#     # Execute JavaScript to get the canvas data URL
#     canvas_data_url = driver.execute_script("""
#         var canvas = document.getElementsByClassName('runner-canvas')[0];
#         return canvas.toDataURL('image/png');
#     """)

    

#     # Decode the base64 data URL to get the image data
#     if canvas_data_url is not None:
#         image_data = base64.b64decode(canvas_data_url.split(',')[1])
        
#     image = Image.open(BytesIO(image_data))

#     # Convert the PIL Image to a numpy array
#     image_array_ = np.array(image)
#     copy= image_array_.copy()
#     image_array = copy[:,:,3]
#     image = image_array
#     width, height = image.shape
#     canvas = np.zeros((int(width),int(height/10)+7))
#     image_copy = image.copy()
#     image_copy[:20,:height]= 0

#     image_copy[:int(width),:int(height/10)+9]= 0
#     kernel = np.ones((4,4), np.uint8)
#     eroded = cv2.erode(image_copy,kernel, iterations=1)
#     dilated = cv2.dilate(eroded,kernel, iterations=2)
#     contours,_ = cv2.findContours(dilated,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     # cv2.drawContours(image, contours, -1, (50, 209, 255), 1)
#     min_area = 40  # Minimum contour area
#     max_area = 3000  # Maximum contour area
#     image_ = cv2.cvtColor(dilated,cv2.COLOR_GRAY2RGB)
#     # Filter contours based on area
#     filtered_contours = [cnt for cnt in contours if min_area <= cv2.contourArea(cnt) <= max_area]
#     x_min=None
#     y_min = None
#     w_min= None
#     h_min= None
#     for contour in filtered_contours:
#         # Get the bounding rectangle for the contour
#         x, y, w, h = cv2.boundingRect(contour)
#         # Draw the rectangle on the original image
#         cv2.rectangle(image_array_, (x, y), (x+w, y+h), (0, 255,0 ), 2)
#         if x_min == None :
#             x_min = x
#             y_min = y
#             h_min = h
#             w_min = w
#             current_time = None
#             current_position___px = None
#         elif x < x_min :
#             x_min = x
#             y_min = y
#             h_min = h
#             w_min = w
#             current_time = time.time()
#             current_position___px = x_min
        
#     if x_min is not None:
#         current_time = time.time()
#     # Define the text and font
#     text = f"w {w_min}, h {h_min}"
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     font_scale = 0.5
#     color = (255, 255, 255)  # White color in BGR
#     thickness = 0

#     # Position (x, y) to start the text

#     position = (x_min, y_min-5) if x_min and y_min else ( 10,10)

#     # Add text to image
#     cv2.putText(image_array_, text, position, font, font_scale, color, thickness, cv2.LINE_AA)
#     cv2.line(image_array_,(int(height/10)+9,y_min),(x_min,y_min),(255,0,0),2)
#     if x_min is not None and y_min is not None :
#         if  x_min < 130   :
#             if h_min > 40 or w_min > 40:
#                 # Press the space button
#                 keyboard.press('space')

#                 # Hold for 0.2 seconds
#                 time.sleep(0.2)

#                 # Release the space button
#                 keyboard.release('space')
#                 print("button pressed")
#             else:

#                 # Press the space button
#                 keyboard.press('space')

#                 # Hold for 0.2 seconds
#                 time.sleep(0.000001)

#                 # Release the space button
#                 keyboard.release('space')
#                 print("button pressed")

#     cv2.imshow('dinosaur',image_array_)
#     # Break the loop if 'q' is pressed
#     # Wait for a key press and check the pressed key
#     key = cv2.waitKey(1) & 0xFF

 
#     # np.save('array' + str(i) + '.npy', image_array)
    
    
#     if key == ord('q'):
#         break

#     i+=1
#     # Sleep for a short time to reduce CPU usage
#     # time.sleep(0.1)
# # Close the WebDriver
# # Specify the filename
# import pandas as pd

# dicto= dict()
# dicto["x_positions"] =  x_positions
# dicto["y_positions"] = y_positions

# # Create DataFrame
# df = pd.DataFrame(dicto)

# # Display DataFrame

# # Save DataFrame to a CSV file
# # df.to_csv('output.csv', index=False)

# driver.quit()
# cv2.destroyAllWindows()


GAME_CANVAS_CLASSNAME = "runner-canvas"
class Obstacl:
    def __init__(self,x,y,w,h) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.j = h

    def speed(self, current_postion___px:int,current_time, previous_position___px:int, previous_time):
        return (current_postion___px-previous_position___px)/(current_time-previous_time) 

def image_scrapper():
    global GAME_CANVAS_CLASSNAME

    # Execute JavaScript to get the canvas data URL
    canvas_data_url = driver.execute_script("""
        var canvas = document.getElementsByClassName('runner-canvas')[0];
        return canvas.toDataURL('image/png');
    """)
     # Decode the base64 data URL to get the image data
    if canvas_data_url is not None:
        image_data = base64.b64decode(canvas_data_url.split(',')[1])
        
    image = Image.open(BytesIO(image_data))

    # Convert the PIL Image to a numpy array
    image_array = np.array(image)

    return image_array

def image_processor(image: np.ndarray):

    copy= image.copy()
    image_array = copy[:,:,3]
    image = image_array
    width, height = image.shape
    canvas = np.zeros((int(width),int(height/10)+7))
    image_copy = image.copy()
    image_copy[:20,:height]= 0

    image_copy[:int(width),:int(height/10)+9]= 0
    kernel = np.ones((4,4), np.uint8)
    eroded = cv2.erode(image_copy,kernel, iterations=1)
    dilated = cv2.dilate(eroded,kernel, iterations=2)
    contours,_ = cv2.findContours(dilated,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(image, contours, -1, (50, 209, 255), 1)
    min_area = 40  # Minimum contour area
    max_area = 3000  # Maximum contour area
    image_ = cv2.cvtColor(dilated,cv2.COLOR_GRAY2RGB)
    # Filter contours based on area
    filtered_contours = [cnt for cnt in contours if min_area <= cv2.contourArea(cnt) <= max_area]
    x_min=None
    y_min = None
    w_min= None
    h_min= None
    for contour in filtered_contours:
        # Get the bounding rectangle for the contour
        x, y, w, h = cv2.boundingRect(contour)
        # Draw the rectangle on the original image
        cv2.rectangle(image_array_, (x, y), (x+w, y+h), (0, 255,0 ), 2)
        if x_min == None :
            x_min = x
            y_min = y
            h_min = h
            w_min = w
            current_time = None
            current_position___px = None
        elif x < x_min :
            x_min = x
            y_min = y
            h_min = h
            w_min = w
            current_time = time.time()
            current_position___px = x_min
        
    if x_min is not None:
        current_time = time.time()
    # Define the text and font
    text = f"w {w_min}, h {h_min}"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.5
    color = (255, 255, 255)  # White color in BGR
    thickness = 0

    # Position (x, y) to start the text

    position = (x_min, y_min-5) if x_min and y_min else ( 10,10)

    # Add text to image
    cv2.putText(image_array_, text, position, font, font_scale, color, thickness, cv2.LINE_AA)
    cv2.line(image_array_,(int(height/10)+9,y_min),(x_min,y_min),(255,0,0),2)

    return image_array_
 
def render(image: np.ndarray, window_name:str):
    cv2.imshow(window_name,image)
    # Wait for a key press and check the pressed key
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        cv2.destroyWindow(window_name)

if __name__ == "__main__":
    i=0
    x_positions= list()
    y_positions = list()
    spacebar_pressed = False
    while True:
        if while_break:
            break
        image_array = image_scrapper()
        processed_image = image_processor(image_array)
        render(processed_image,WINDOW_NAME)
    driver.quit()
    cv2.destroyAllWindows()