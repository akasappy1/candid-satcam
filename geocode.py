from geopy.geocoders import Nominatim
from time import sleep
geocoder = Nominatim(user_agent="ur_on_candid_satcam")

def get_long_lat(input_address):
    """Gets a longitude and latitude from a user-input address."""
    location = geocoder.geocode(input_address)
    if location:
        long = location.longitude
        lat = location.latitude
        print(f"Longitude: {long}")
        print(f"Latitude: {lat}")
        return long, lat
    else:
        print("Address wasn't properly formatted, please doublecheck and re-enter address.")
    sleep(1.5)