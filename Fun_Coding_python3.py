# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 14:34:39 2024

@author: Morteza
"""

import cv2
import numpy as np
import random
import ctypes

# Get the monitor resolution
user32 = ctypes.windll.user32
width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# Define font properties
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 6
font_thickness = 10

# Define text
text = "Coding is fun"

# Initialize position and direction of the text
x = 0
y = height // 2  # Center vertically
direction = 1  # Moving from left to right

# Create a video writer
out = cv2.VideoWriter('coding_in_python.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

while True:
    # Create a black image
    image = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Generate random color for the text
    text_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    # Render text on the image
    cv2.putText(image, text, (x, y), font, font_scale, text_color, font_thickness)
    
    # Generate random lights
    for _ in range(50):
        lx = random.randint(0, width - 1)
        ly = random.randint(0, height - 1)
        light_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv2.circle(image, (lx, ly), 2, light_color, -1)
    
    # Show the image
    cv2.imshow('Coding in Python', image)
    
    # Write the frame to the video writer
    out.write(image)
    
    # Move the text
    x += direction * 10
    
    # Make the text move slightly up and down
    y += random.randint(-3, 3)
    y = max(0, min(y, height - 100))  # Ensure text stays within the screen
    
    # Check if the text has reached the end of the screen
    if x >= width - 600:  # Assuming the approximate width of the text
        direction = -1  # Move text to the left
    elif x <= 0:
        direction = 1   # Move text to the right
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release the video writer and close the OpenCV window
out.release()
cv2.destroyAllWindows()
