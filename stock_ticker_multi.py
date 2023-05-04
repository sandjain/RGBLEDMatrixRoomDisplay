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

stock_symbols = ['YOUR', 'STOCK', 'TICKER', 'SYMBOLS', 'HERE']

def get_stock_price(stocks):
	
	stock_metric_list = []
	
	for stock in stocks:
		stock_metric_tuple = ()
		url = f'https://finance.yahoo.com/quote/{stock}'
		response = requests.get(url)
		soup = BeautifulSoup(response.text, 'html.parser')
		price_element = soup.find('fin-streamer', {'data-symbol':f'{stock}','data-field':'regularMarketPrice'})
		percentage_element = soup.find('fin-streamer', {'data-symbol':f'{stock}','data-field':'regularMarketChangePercent'})
		#stock_prices.append(float(price_element['value']))
		#stock_percentage_change.append(round(float(percentage_element['value']),2))
		stock_metric_tuple = (round(float(price_element['value']),2), round(float(percentage_element['value'])*100,2))
		stock_metric_list.append(stock_metric_tuple)
	stock_dict = dict(zip(stocks,stock_metric_list))
	return stock_dict

def display_stock_ticker(stock_symbols):
	stock_ticker_dict = get_stock_price(stock_symbols)
	offscreen_canvas = matrix.CreateFrameCanvas()
	#if you want to keep it going remove the comment on the next line
	#while True:
	for symbol, stock_metric in stock_ticker_dict.items():
		if stock_metric[1] < 0:
			text_color = graphics.Color(255,0,0)
			message = f'{symbol}:${stock_metric[0]} {stock_metric[1]}%'
		else:
			text_color = graphics.Color(0,255,0)
			message = f'{symbol}:${stock_metric[0]} +{stock_metric[1]}%'
		pos = offscreen_canvas.width
		length = graphics.DrawText(offscreen_canvas, font, pos, 20, text_color, message)
		while (pos + length) >= 0:
			try:
				#message = 'priya rules! happy bridal shower!'
				offscreen_canvas.Clear()
				pos -= 1
				length = graphics.DrawText(offscreen_canvas, font, pos, 20, text_color, message)
				time.sleep(0.02)
				offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
			except Exception as e:
				print(f'Error fetching stock price: {e}')
				time.sleep(10)

if __name__ ==  "__main__":
	
	display_stock_ticker(stock_symbols)


