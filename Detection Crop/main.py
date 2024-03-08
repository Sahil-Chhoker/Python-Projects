import numpy as mp
import cv2 as cv
from matplotlib import pyplot as plt

# Watershed algorithm

# step-1: convert to greyscale
img_path = 'C:\MASTER FOLDER\Python-Projects\Detection Crop\dino_assets.png'
sprite = cv.imread(img_path)
assert sprite is not None, "file could not be read, check with os.path.exists()"

gray = cv.cvtColor(sprite, cv.COLOR_BGR2GRAY)
# ret, thrash = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)      // NO NEED FOR OTSU's BINARIZATION in this file
cv.imshow("hi", gray)
cv.waitKey(0)