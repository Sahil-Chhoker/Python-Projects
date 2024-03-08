import os
import cv2 as cv
sprite = cv.imread('C:\MASTER FOLDER\Python-Projects\Image Slitter\db35jhmr.png')
sprite_list = []

for i in range(0, 1000, 100):
    crop_sprite = sprite[0:1000, i:i+100]
    sprite_list.append(crop_sprite)

os.chdir('C:\MASTER FOLDER\Python-Projects\Image Slitter')
for i in range(len(sprite_list)):
    cv.imwrite(f"{i}.png", sprite_list[i])