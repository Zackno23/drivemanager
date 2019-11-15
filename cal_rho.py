import numpy as np


def cal_rho(lon_a, lat_a, lon_b, lat_b):
    from math import sin, cos, sqrt, atan2, radians

    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lon_a)
    lon1 = radians(lon_b)
    lat2 = radians(lat_a)
    lon2 = radians(lat_b)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance
    # print("Result:", distance)
    # print("Should be:", 278.546, "km")
