import os
import cv2 as cv

image_path = 'C:\MASTER FOLDER\Python-Projects\Image Slitter\db35jhmr.png'
save_path = 'C:\MASTER FOLDER\Python-Projects\Image Slitter'
sprite = cv.imread(image_path)
im_length, im_width, im_channel = sprite.shape

sprite_list = []

step = int(input("Write the step you want in the cropping : "))

# clean up
if step == 0:
    i = 0
    try:
        while f'C:\MASTER FOLDER\Python-Projects\Image Slitter\{i}.png':
            os.remove(f'C:\MASTER FOLDER\Python-Projects\Image Slitter\{i}.png')
            i += 1
    except:
        print("All files are sucessfully deleted")
        
else:
    for i in range(0, im_width, step):
        crop_sprite = sprite[0:im_length, i:i+step]
        sprite_list.append(crop_sprite)

    os.chdir(save_path)
    for i in range(len(sprite_list)):
        cv.imwrite(f"{i}.png", sprite_list[i])
