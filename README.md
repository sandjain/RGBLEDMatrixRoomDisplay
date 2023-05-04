# RGBLEDMatrixRoomDisplay
Programming a RGB LED matrix to display personally relevant daily information (eg, local weather, stock prices, relevant news headlines) similar to a phone's welcome screen or web browser's homepage.

There are a few different displays that have programmed thus far, including a news ticker (makes use of the NewsCatherAPI), a stock ticker (from yahoo finance), a estimated commute time to work (uses Google Maps matrix API), and a weather display (uses the OpenWeatherMap API). Between the displays are random GIF transitions selected from a personal collection of GIFs to make the transitions from one screen to the next a bit more fun and entertaining.

The script_switcher.py script transitions between different programs, each responsible for a different display (described above).

#News Ticker
The news ticker makes use of the newscatcher api to grab relevant top headlines and display them in a scrolling ticker fashion. This information is purely for personal use for this project and not for any data collection or monetized use. The program calls to the API about once every 2-3 minutes to make sure the most up-to-date headlines are pulled. 

#Stock Ticker
The program that controls this display uses the Beautiful Soup library to search the yahoo finance website for the current stock price and percentage change since the prior day's closing price. The stock price and percentage change for a given stock ticker scroll across the display in a pre-defined sequence. There is no limit to how many stocks can be displayed.

#Weather Display
The program that controls the weather display makes use of the free OpenWeather API. The program makes a new call to the API with each cycle of the display. The display screen shows the current temperature, predicted low and high temperatures for the specified city for the specified day. It also shows the weather condition. Based on the weather condition, it displays a .png image that corresponds to the weather condition (a picture of a cloud if the current condition is "cloudy").
