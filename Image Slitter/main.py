import os
import cv2 as cv

image_path = 'C:\MASTER FOLDER\Python-Projects\Image Slitter\db35jhmr.png'
save_path = 'C:\MASTER FOLDER\Python-Projects\Image Slitter'
sprite = cv.imread(image_path)
sprite_list = []

step = int(input("Write the step you want in the cropping : "))

im_length, im_width, im_channel = sprite.shape

for i in range(0, im_width, step):
    crop_sprite = sprite[0:im_length, i:i+step]
    sprite_list.append(crop_sprite)

os.chdir(save_path)
for i in range(len(sprite_list)):
    cv.imwrite(f"{i}.png", sprite_list[i])