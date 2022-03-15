#!/usr/bin/env python3

import os
import re
import requests

url = 'http://34.72.96.18/fruits/'
src = 'supplier-data/descriptions'

def upload(fruit):
    '''Uploads dictionary fruit contents using POST'''
    resp = requests.post(url, data = fruit)
    print('{} -> {}'.format(fruit['name'], resp.status_code))

def get_fruit(textfile):
    '''Return the fruit dictionary with file contents'''
    fruit = {}
    with open(textfile, 'r') as file:
        fruit['name'] = file.readline().strip()
        fruit['weight'] = int( re.search(r'(\d+)', file.readline())[1] )
        fruit['description'] = file.readline().strip()
    fruit['image_name'] = textfile.replace('txt', 'jpeg')
    return fruit

def main():
    '''Iterate through files and pass to get_fruit, then uploads'''
    os.chdir(src)
    for textfile in os.listdir():
        fruit = get_fruit(textfile)
        upload(fruit)

main()
