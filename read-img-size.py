#!/usr/bin/env python3


from PIL import Image
import sys
import os

def main():

    user_input = input("Enter the image folder path: ")
    dir_user = sorted(os.listdir(user_input))

    #print(dir_user)
    
    for image_path in dir_user:
       if not image_path.startswith('.'):
                
       # join folder and file path
        input_path = os.path.join(user_input, image_path)
        
       # get the size and print filename and size
        image_size = Image.open(input_path).size
        print('Image name: ', input_path, '\n', 'Size (Width, Height): ', image_size)
       
if __name__ == '__main__':
    main()
