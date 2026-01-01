
import pandas as pd
import herbie
import os
import sys

def suppress_output(): # Wrapper to hide Herbie output from casual users.
    sys.stdout = open(os.devnull, 'w')

def enable_output():
    sys.stdout = sys.__stdout__

def is_visibility_ok(lat, long, date):
    """Queries GFS model forecast via Herbie to get daytime cloudcover estimates for user's input location."""
    suppress_output()
    H = herbie.Herbie(date, verbose=False)
    global_cloud_cover = H.xarray(r":TCDC:e")
    location = pd.DataFrame(
        {
            "latitude": [lat],
            "longitude": [long],
        }
    )
    # if 'crs' in global_cloud_cover.coords:
    #     print(global_cloud_cover.coords['crs'])
    # print(global_cloud_cover.coords)
    local_cloud_cover = global_cloud_cover.herbie.pick_points(points=location, method="nearest")
    # print(local_cloud_cover)
    cloud_cover_val = local_cloud_cover["tcc"].item()
    # print(cloud_cover_val)
    enable_output()
    if cloud_cover_val >= 40:
        return False
    elif cloud_cover_val < 40:
        return True
    
    
