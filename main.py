from geocode import get_long_lat

# prompt user for a cleanly formatted address for geocoding.
user_address = input("Please enter your address in the following format.\n'123 Main Street, Anytown, State, 00000, USA'\n")
get_long_lat(user_address) #geocode the address
