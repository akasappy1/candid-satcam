import pytz
import datetime
from timezonefinder import TimezoneFinder 
from geopy.geocoders import Nominatim
from time import sleep
geocoder = Nominatim(user_agent="ur_on_candid_satcam")

tf = TimezoneFinder()

def get_long_lat(input_address):
    """Gets a longitude and latitude from a user-input address."""
    location = geocoder.geocode(input_address)
    if location:
        long = location.longitude
        lat = location.latitude
        tz = tf.timezone_at(lng=long, lat=lat)
        raw_date = datetime.date.today()
        date = raw_date.isoformat()
        if tz:
            # print(f"Longitude: {long}")
            # print(f"Latitude: {lat}")
            # print(f"Timezone: {tz}")
            # print(f"Request Date: {date}")
            coords = [lat, long, date, tz]
            return coords
        else:
            print("Got correct coordinates in decimal degrees, but was unable to identify correct timezone, please try again.")
    else:
        print("Address wasn't properly formatted, please doublecheck and re-enter address.")
    sleep(1.5)

