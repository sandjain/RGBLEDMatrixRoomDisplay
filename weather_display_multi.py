import requests
import time
import requests
from bs4 import BeautifulSoup
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from PIL import Image

options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat-pwm'
options.brightness =  70
options.gpio_slowdown = 4
matrix = RGBMatrix(options=options)
font = graphics.Font()
font.LoadFont('/home/pi/rpi-rgb-led-matrix/fonts/4x6.bdf')
text_color_now = graphics.Color(255, 219,88)
text_color_hi = graphics.Color(255,75,75)
text_color_low = graphics.Color(75,75,255)

#thunderstorm, drizzle, rain, snow, clear, clouds

sun_image = Image.open('/home/pi/ledMatrixProjects/sun.png')
thunderstorm_image = Image.open('/home/pi/ledMatrixProjects/thunderstorm.png')
drizzle_image = Image.open('/home/pi/ledMatrixProjects/drizzle.png')
rain_image = Image.open('/home/pi/ledMatrixProjects/rain.png')
snow_image = Image.open('/home/pi/ledMatrixProjects/snow.png')
clouds_image = Image.open('/home/pi/ledMatrixProjects/clouds.png')

x_pos = 0
y_pos = font.baseline + 1


API_KEY = 'YOUR API KEY HERE'

CITY_NAME = 'YOUR CITY NAME HERE'
STATE_CODE = 'YOUR STATE CODE HERE'
COUNTRY_CODE = '840'

GEO_CODING_BASE_URL = 'http://api.openweathermap.org/geo/1.0/direct?'

WEATHER_BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

geourl = f'{GEO_CODING_BASE_URL}q={CITY_NAME}&appid={API_KEY}'

geo_response = requests.get(geourl)

if geo_response.status_code == 200:
	geo_data = geo_response.json()
	#print(geo_data)
else:
	print(f'Error: {geo_response.status_code}')

LATITUDE = geo_data[0]['lat']
LONGITUDE = geo_data[0]['lon']

weatherurl = f'{WEATHER_BASE_URL}lat={LATITUDE}&lon={LONGITUDE}&appid={API_KEY}'

weather_response = requests.get(weatherurl)

if weather_response.status_code == 200:
	weather_data = weather_response.json()
	#print(weather_data)
else:
	print(f'Error: {weather_response.status_code}')

K_TEMPERATURE = weather_data['main']['temp']
K_TEMPERATURE_MAX = weather_data['main']['temp_max']
K_TEMPERATURE_MIN = weather_data['main']['temp_min']


WEATHER_MAIN = weather_data['weather'][0]['main'].lower()
WEATHER_DESC = weather_data['weather'][0]['description'].lower()

def KelvinToFormFar(Ktemp):
	fartemp = 1.8*(Ktemp-273)+32
	formtemp = "{:.0f}".format(fartemp)
	return formtemp

def drawImage(weather_image):
	weather_image.thumbnail((50,50),Image.ANTIALIAS)
	for x in range(weather_image.width):
    		for y in range(weather_image.height):
        		r, g, b, a = weather_image.getpixel((x, y))
        		matrix.SetPixel(x+43, y+4, r, g, b)


F_TEMPERATURE_NOW = KelvinToFormFar(K_TEMPERATURE)
F_TEMPERATURE_MAX = KelvinToFormFar(K_TEMPERATURE_MAX)
F_TEMPERATURE_MIN = KelvinToFormFar(K_TEMPERATURE_MIN)

#Remove the comment for the while True if you want the weather to display forever 
#while True:
length1 = graphics.DrawText(matrix, font, x_pos, y_pos, text_color_now, f'now: ')
graphics.DrawText(matrix, font, x_pos+length1+1, y_pos, text_color_now, f'{F_TEMPERATURE_NOW}F')
length2 = graphics.DrawText(matrix, font, x_pos, y_pos+7, text_color_now, f'high:')
graphics.DrawText(matrix,font,x_pos+length2+1, y_pos+7, text_color_hi, f'{F_TEMPERATURE_MAX}F')
length3 = graphics.DrawText(matrix, font, x_pos, y_pos+14, text_color_now, f'low: ')
graphics.DrawText(matrix,font,x_pos+length3+1, y_pos+14, text_color_low, f'{F_TEMPERATURE_MIN}F')
graphics.DrawText(matrix,font,x_pos, y_pos+21, text_color_now, f'{WEATHER_DESC}')
if WEATHER_MAIN == 'clear':
	drawImage(sun_image)
elif WEATHER_MAIN == 'thunderstorm':
	drawImage(thunderstorm_image)
elif WEATHER_MAIN == 'drizzle':
	drawImage(drizzle_image)
elif WEATHER_MAIN == 'rain':
	drawImage(rain_image)
elif WEATHER_MAIN == 'snow':
	drawImage(snow_image)
elif WEATHER_MAIN == 'clouds':
	drawImage(clouds_image)

time.sleep(10)

#print(f"It's {F_TEMPERATURE_NOW}F outside right now with a high of {F_TEMPERATURE_MAX}F and a low of {F_TEMPERATURE_MIN}F")
