import time
from PIL import Image, ImageSequence
from rgbmatrix import RGBMatrix, RGBMatrixOptions

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat-pwm'
options.brightness =  40
options.gpio_slowdown = 4
matrix = RGBMatrix(options=options)

# Open the gif
im = Image.open('unicorn.gif')

for i in range(4): 
# Iterate through the frames
    for frame in ImageSequence.Iterator(im):
        frame = frame.convert('RGB')

        # Create an image that will be the correct size for the display
        display_image = Image.new('RGB', (options.rows, options.cols))

        # Paste our frame into this image
        display_image.paste(frame)

        # Set the image to the matrix
        matrix.SetImage(display_image)

        # Sleep for a bit between frames
        time.sleep(0.05)  # adjust this to change the speed of your animation
