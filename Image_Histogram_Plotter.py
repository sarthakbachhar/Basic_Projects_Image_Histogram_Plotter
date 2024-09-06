import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image in grayscale 
img = cv2.imread('C:/Users/Acer/Desktop/Tiger.jpeg', 0)

# Check if the image was successfully loaded 
if img is None:
  print("Unable to load image.")
  
else:
  # Calculate the histogram
  hist = cv2.calcHist([img], [0], None, [256], [0,256])

  # Plot the values
  plt.plot(hist)
  plt.title("Grayscale Histogram")
  plt.xlabel("Pixel Intensity")
  plt.ylabel("Frequency")
  
  # Display the values
  plt.show()
