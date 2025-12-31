
import pandas as pd
import herbie

def get_cloud_cover(lat, long, date):
    """Queries GFS model forecast via Herbie to get daytime cloudcover estimates for user's input location."""
    H = herbie.Herbie(date)
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
    print(local_cloud_cover)
    cloud_cover_val = local_cloud_cover["tcc"].item()
    print(cloud_cover_val)
    
get_cloud_cover(44.27, -71.30, "2025-12-30")