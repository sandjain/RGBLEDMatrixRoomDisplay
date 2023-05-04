from newscatcherapi import NewsCatcherApiClient
import random
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
options.brightness =  60
options.gpio_slowdown = 4
matrix = RGBMatrix(options=options)
font = graphics.Font()
font.LoadFont('/home/pi/rpi-rgb-led-matrix/fonts/5x8.bdf')
text_color = graphics.Color(90,255,150)


newscatcherapi = NewsCatcherApiClient(x_api_key='YOUR KEY GOES HERE')
clean_urls = ['nytimes.com','bbc.com', 'cnn.com', 'msnbc.com']

def get_headline(clean_urls):
    aggregated_articles = newscatcherapi.get_latest_headlines(topic='news',
                                    page_size = 20,
                                    sources = clean_urls,
                                    lang = 'en',
                                    page = 1)

    summary = aggregated_articles['articles'][random.choice(range(10))]['summary']
    summary = summary.replace('\n','')
    return summary

def display_news_headline(clean_urls):
    news_headline = get_headline(clean_urls)
    offscreen_canvas = matrix.CreateFrameCanvas()
    #if you want to keep it going remove the comment on the next line
    #while True:
    pos = offscreen_canvas.width
    length = graphics.DrawText(offscreen_canvas, font, pos, 20, text_color, news_headline)
    while (pos + length) >= 0:
        try:
            #message = 'priya rules! happy bridal shower!'
            offscreen_canvas.Clear()
            pos -= 1
            length = graphics.DrawText(offscreen_canvas, font, pos, 20, text_color, news_headline)
            time.sleep(0.01)
            offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
        except Exception as e:
            print(f'Error fetching headline: {e}')
            time.sleep(10)

if __name__ ==  "__main__":
    display_news_headline(clean_urls)


