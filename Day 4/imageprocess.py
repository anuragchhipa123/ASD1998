# -*- coding: utf-8 -*-
"""
Created on Fri May 10 22:43:48 2019

@author: DELL
"""

from PIL import Image
import os

img=Image.open("a.jpg")
img_rotate = img.transpose(Image.ROTATE_90)
img_rotate.show()

crop_im = img.crop(box=(160,12,240,34))
crop_im.save('a.jpg')
crop_im.show()

img.thumbnail((75, 75))
print(img.width, img.height)
img.save('a.jpg')
img.show()