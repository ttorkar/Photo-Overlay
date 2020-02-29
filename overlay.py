# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 02:15:23 2020

@author: Guest2018_93
"""
from PIL import Image, ImageOps
import os

logo = Image.open('logo.png')
# resize the image
size = (80,35)
logo = logo.resize(size,Image.ANTIALIAS)


for i, subdir in enumerate([x[0] for x in os.walk('.')]):
    print(i, subdir)
    if i == 0: continue
    for file in os.listdir(subdir):
        print("Image: ", file)
        background = Image.open(subdir +'/' + file)
        background_temp = background.copy()
        width, height = background_temp.size
        background_temp.paste(logo, (width-size[0] - 10, height-size[1] - 10), logo)
        
        newdir = subdir + '_with_overlay'
        if os.path.exists(newdir) == False: os.mkdir(newdir)
        
        background_temp.save(newdir +'/' + file,"PNG")