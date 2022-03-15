#!/usr/bin/env python3

from PIL import Image
import os
import re

src = 'supplier-data/images/'

def convert_image(filename):
    '''Converts image from .tiff to .jpeg and from 3000x2000 to 600x400'''
    filename_dest = filename.replace('.tiff', '.jpeg')
    img = Image.open(filename).convert('RGB').resize((600,400))
    img.save(filename_dest, format='JPEG')
    print('Converted file "{}" to "{}"'.format(filename, filename_dest))

def main():
    '''Iterates through images and convert them'''
    os.chdir(src)
    for img in os.listdir():
        if re.search(r'\.tiff$', img):
            convert_image(img)

main()
