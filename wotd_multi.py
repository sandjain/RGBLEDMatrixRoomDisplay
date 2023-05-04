import time
import requests
from bs4 import BeautifulSoup
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat-pwm'
options.brightness =  40
options.gpio_slowdown = 4
matrix = RGBMatrix(options=options)
font = graphics.Font()
font.LoadFont('/home/pi/rpi-rgb-led-matrix/fonts/6x10.bdf')
text_color = graphics.Color(0,255,0)

def get_wotd():
	stock_metric_list = []
	url = f'https://www.merriam-webster.com/word-of-the-day'
	response = requests.get(url)

	if response.status_code == 200:

	    # Get the content of the response
	    content = response.content

	    # Create a BeautifulSoup object and specify the parser
	    soup = BeautifulSoup(content, 'html.parser')

		html_code = soup.find('h2', class_ = 'word-header-txt')
		word = html_code.get_text()
		return word
	else:
		print('Error getting response')

if __name__ ==  "__main__":
	get_wotd()
