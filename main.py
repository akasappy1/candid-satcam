from geocode import get_long_lat
from is_visible import is_visibility_ok
from get_wrs_path import find_wrs_path, get_revisit_day
from get_landsat_date import get_landsat_date, get_days_to_revisit


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
            # print(f"Satellites could see you today: {area_viz}")
            # if area_viz == True:
            user_path, user_row = find_wrs_path(geocoded_addr[0], geocoded_addr[1])
            # print(f"Your WRS Path number(s): {user_path}")
            # print(f"Your WRS Row number(s): {user_row}")
            user_revisits= get_revisit_day(user_path)
            # print(f"Your revisit cycle day(s): {user_revisits}")
            landsat_today = get_landsat_date()
            next_landsat_visit = get_days_to_revisit(landsat_today, user_revisits)
            # print(f"Your next revisit is in {next_landsat_visit} days. Get ready!")
            if area_viz == True and next_landsat_visit == 0:
                print("You're on Candid Landsat (9)! Put on an outfit--and don't forget to wave!")
            elif area_viz == True and next_landsat_visit > 0:
                print("It's a great day for satellites, but Landsat 9 isn't here right now.")
                print(f"But you have {next_landsat_visit} days to prep for Landsat 9's next visit. How about some yard work? (Seriously, touch some grass.)")
            elif area_viz == False and next_landsat_visit == 0:
                print("Landsat 9 is here, but so are those pesky clouds--shielding you from its all-seeing eye. Better luck next time!")
            elif area_viz == False and next_landsat_visit > 0:
                print(f"The weather gods are angry, but you still have {next_landsat_visit} days to win their favor before Landsat 9 visits.")
                print("Have you thought about sacrificing a GNSS device in their honor?")
            


