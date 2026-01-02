import datetime

 
EPOCH_START = datetime.date(2000, 1, 6)

def get_landsat_date():
    """Fetches the current day's LANDSAT revisit cycle number. Does not accept an input for now."""
    date = datetime.date.today()
    
    num_days_delta = date - EPOCH_START
    num_days = num_days_delta.days
    landsat_date = num_days % 16 + 1 # Mod division by 16 because that's Landsat's revisit cycle length, add one because visit days aren't 0-indexed.
    # print(landsat_date)
    return landsat_date

def get_days_to_revisit(landsat_date, revisit_days):
    """Accepts a current landsat date and a list of revisit days for a specific point (and its Landsat paths), and calculates the nearest return."""
    min_time = 15 # Sets the maximum number of days until user is revisited by Landsat 9
    for day in revisit_days:
        if day == landsat_date:
            return 0 # today is user's landsat visit date, no need to check other days.
        else:
            num_days = abs(landsat_date - day) # Find the next revisit date if not today.
            if num_days < min_time:
                min_time = num_days
    return min_time