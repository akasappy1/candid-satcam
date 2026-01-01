from geocode import get_long_lat
from is_visible import is_visibility_ok


print("Hello! You can use this program to see whether you're on candida (Landsat) camera today!")
print("Enter 'quit' any time to quit.")
# prompt user for a cleanly formatted address for geocoding.
while True:
    user_address = input("Please enter your address in the following format.\n'123 Main Street, Anytown, State, 00000, USA'\n")
    if user_address.lower() == "quit":
        break
    else:
        geocoded_addr = get_long_lat(user_address) #geocode the address
        print(geocoded_addr)
        # check for 40% or less cloud cover using the is_visibility_ok function
        if geocoded_addr:
            area_viz = is_visibility_ok(geocoded_addr[0], geocoded_addr[1], geocoded_addr[2])
            print(f"Satellites could see you today: {area_viz}")


