import time
from PIL import Image, ImageSequence
from rgbmatrix import RGBMatrix, RGBMatrixOptions
import random
import os
import glob

def find_files(folder_path, file_extension):
    file_names = []
    os.chdir(folder_path)
    for file in glob.glob(f"*.{file_extension}"):
        file_names.append(file)
    return file_names

# Call the function with the folder path and file extension you want
gif_names = find_files('/home/pi/ledMatrixProjects', 'gif')

random_gif = random.choice(gif_names)

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat-pwm'
options.brightness =  80
options.gpio_slowdown = 4
matrix = RGBMatrix(options=options)

# Open the gif
im = Image.open(f'{random_gif}')

for i in range(4): 
# Iterate through the frames
    for frame in ImageSequence.Iterator(im):
        # Convert the image to RGB
        frame = frame.convert('RGB')
        frame.thumbnail((options.rows,options.cols))
        #resized_frame = frame.resize((options.rows, options.rows))
        #print(frame.size)
        # Create an image that will be the correct size for the display
        #display_image = Image.new('RGB', (options.rows, options.cols))
        if frame.size[1] < options.rows:
            pos_y = (options.rows-frame.size[1])//2
        else:
            pos_y = 0

        if frame.size[0] < options.cols:
            pos_x = (options.cols-frame.size[0])//2
        else:
            pos_x = 0

        #print((pos_x, pos_y))
        # Paste our frame into this image
        #display_image.paste(resized_frame)

        # Set the image to the matrix
        matrix.SetImage(frame, offset_x = pos_x, offset_y = pos_y)

        # Sleep for a bit between frames
        time.sleep(0.07)  # adjust this to change the speed of your animation
