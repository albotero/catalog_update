#!/usr/bin/env python3

import os
import re
import requests

url = "http://localhost/upload/"
src = 'supplier-data/images/'

def upload(filename):
    try:
        with open(filename, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
        print('Uploaded image "{}"'.format(filename))
    except Exception as ex:
        print('ERROR: {}', ex)

def main():
    os.chdir(src)
    for img in os.listdir():
        if re.search(r'\.jpeg$', img):
            upload(img)

main()
