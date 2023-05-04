import googlemaps
from googlemaps.exceptions import ApiError, TransportError, Timeout
from datetime import datetime, timedelta

# Define the API Key.
API_KEY = 'YOUR API KEY GOES HERE'

# Define the Client
gmaps = googlemaps.Client(key = API_KEY)

# Define the home and work addresses.
my_home = 'YOUR HOME ADDRESS HERE'
my_work = 'YOUR WORK ADDRESS HERE'

# Get the current date and time
now = datetime.now()

# Create a new datetime object for the desired departure time on the current date
departure_time = datetime(now.year, now.month, now.day, 9)  # 9 AM

# If the current time is past 9 AM, set the departure time to 9 AM tomorrow
if now > departure_time:
    departure_time += timedelta(days=1)

try:
    # Request directions.
    directions_result = gmaps.directions(my_home, my_work, departure_time=departure_time)

    # Check if result is empty
    if not directions_result:
        print(f"No route found between {my_home} and {my_work}.")
        exit(1)

    # The result is a list of direction information. 
    # For most scenarios, you would be interested in the first (and likely only) result.
    first_result = directions_result[0]

    # Each result is divided into "legs" for each part of the journey.
    # In a simple journey from point A to point B, there is only one leg.
    first_leg = first_result['legs'][0]

    # You can then access duration information from the leg.
    duration = first_leg['duration']

    # Duration information is in a dictionary-like format.
    # "text" is a human-readable version of the duration, and "value" is the time in seconds.
    print(f"The journey from {my_home} to {my_work} takes {duration['text']} if you leave at {departure_time}.")

    # If you want to handle the time in seconds in your program, you can use duration['value'].

except ApiError as e:
    print(f"API error occurred: {e}")
except TransportError as e:
    print(f"Transport error occurred: {e}")
except Timeout as e:
    print(f"Request timed out: {e}")
