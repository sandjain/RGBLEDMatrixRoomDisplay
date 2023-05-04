import time
import requests
from datetime import datetime
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat-pwm'
options.brightness =  50
options.gpio_slowdown = 4
matrix = RGBMatrix(options=options)

font_date = graphics.Font()
font_date.LoadFont('/home/pi/rpi-rgb-led-matrix/fonts/5x8.bdf')

font_time = graphics.Font()
font_time.LoadFont('/home/pi/rpi-rgb-led-matrix/fonts/5x8.bdf')

text_color = graphics.Color(50, 200,150)

current_date = datetime.now().strftime("%a, %b %d")

x_pos_date = 0
y_pos_date = 8

y_pos_time = 25

seconds_passed = 0

while seconds_passed < 12:
	matrix.Clear()
	current_time = datetime.now().strftime("%H:%M:%S%p")
	x_pos_time = 0
	graphics.DrawText(matrix, font_date, x_pos_date, y_pos_date, text_color, f'{current_date}')
	graphics.DrawText(matrix, font_time, x_pos_time, y_pos_time, text_color, f'{current_time}')
	time.sleep(1)
	seconds_passed += 1