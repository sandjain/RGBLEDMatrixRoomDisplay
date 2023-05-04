import subprocess
import time

while True:
    #print("Running script1.py...")
    subprocess.call(["python3", "weather_display_multi.py"]) # you can replace "python" with "python3" or the specific python interpreter in your system
    time.sleep(0.3) # sleep for 1 second

    subprocess.call(["python3", "gif_multi.py"]) # you can replace "python" with "python3" or the specific python interpreter in your system
    time.sleep(0.2) # sleep for 1 second    

    #print("Running script2.py...")
    subprocess.call(["python3", "stock_ticker_multi.py"])
    time.sleep(0.3) # sleep for 1 second

    subprocess.call(["python3", "gif_multi.py"]) # you can replace "python" with "python3" or the specific python interpreter in your system
    time.sleep(0.2) # sleep for 1 second

    subprocess.call(["python3", "time_display_multi.py"])
    time.sleep(0.3) # sleep for 1 second

    subprocess.call(["python3", "gif_multi.py"]) # you can replace "python" with "python3" or the specific python interpreter in your system
    time.sleep(0.2) # sleep for 1 second

    subprocess.call(["python3", "news_ticker_multi.py"])
    time.sleep(0.3) # sleep for 1 second

    subprocess.call(["python3", "gif_multi.py"]) # you can replace "python" with "python3" or the specific python interpreter in your system
    time.sleep(0.2) # sleep for 1 second