import geopandas as gpd
from shapely.geometry import Point

LANDSAT_DESCENT = r"OrbitShps/WRS2_descending.shp" # This is the relative path to the orbital path file--change or move it at your own risk!
landsat_paths = gpd.read_file(LANDSAT_DESCENT)


def find_wrs_path(lat, long):
    """Compares location point to shapefile to return correct WRS path. Takes a latitude and a longitude (geococed from user input and returns a path number.)"""
    user_point = Point(long, lat)
    intersections = landsat_paths.intersects(user_point)
    intersecting_paths = landsat_paths[intersections]
    paths_list = intersecting_paths['PATH'].to_list()
    rows_list = intersecting_paths['ROW'].to_list()
    return paths_list, rows_list

# The following are constant variables containing lists of the paths covered by landsat 9 on each day of the revisit cycle.
DAY_1 = [102, 118, 124, 150, 166, 182, 198, 214, 230, 13, 29, 45, 61, 77, -1]
DAY_2 = [93, 109, 125, 141, 157, 173, 189, 205, 221, 4, 20, 36, 62, 68, 84, -2]
DAY_3 = [100, 116, 132, 148, 164, 180, 196, 212, 228, 11, 27, 43, 59, 75, -2]
DAY_4 = [91, 107, 123, 139, 155, 171, 187, 203, 219, 2, 18, 34, 50, 66, 82, -4]
DAY_5 = [98, 114, 130, 146, 162, 178, 194, 210, 226, 9, 25, 41, 57, 73, 89, -5]
DAY_6 = [105, 121, 137, 153, 169, 185, 201, 217, 233, 16, 32, 48, 64, 80, -6]
DAY_7 = [96, 112, 128, 144, 160, 176, 192, 208, 224, 7, 23, 39, 55, 71, 87, -7]
DAY_8 = [103, 119, 135, 151, 167, 183, 199, 215, 231, 14, 30, 46, 62, 78, -8]
DAY_9 = [94, 110, 126, 142, 158, 174, 190, 206, 222, 5, 21, 37, 53, 69, 85, -9]
DAY_10 = [101, 117, 133, 149, 165, 181, 197, 213, 229, 12, 28, 44, 60, 76, -10]
DAY_11 = [92, 108, 124, 140, 156, 172, 188, 204, 220, 3, 19, 35, 51, 67, 83, -11]
DAY_12 = [99, 115, 131, 147, 163, 179, 195, 211, 227, 10, 26, 42, 58, 74, -12]
DAY_13 = [90, 106, 122, 138, 154, 170, 186, 202, 218, 1, 17, 33, 49, 65, 81, -13]
DAY_14 = [97, 113, 129, 145, 161, 177, 193, 209, 225, 8, 24, 40, 56, 72, 88, -14]
DAY_15 = [104, 120, 136, 152, 168, 184, 200, 216, 232, 15, 31, 47, 63, 79, -15]
DAY_16 = [111, 127, 143, 159, 175, 191, 207, 223, 6, 22, 38, 54, 70, 86, 95, -16]

ALL_DAYS = [DAY_1, DAY_2, DAY_3, DAY_4, DAY_5, DAY_6, DAY_7, DAY_8, DAY_9,
            DAY_10, DAY_11, DAY_12, DAY_13, DAY_14, DAY_15, DAY_16]

def get_revisit_day(paths_list):
    """From a Landsat Path in the WRS, checks which revisit cycle day that path/point is visited on."""
    visit_days = []
    for path in paths_list:
        for day in ALL_DAYS:
            if path in day:
                day_num = day[-1] * -1
                visit_days.append(day_num)
    return visit_days