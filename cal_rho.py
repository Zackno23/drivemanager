from math import sin, cos, acos, radians

earth_rad = 6378.137


def latlng_to_xyz(lat, lng):
    rlat, rlng = radians(lat), radians(lng)
    coslat = cos(rlat)
    return coslat * cos(rlng), coslat * sin(rlng), sin(rlat)


def dist_on_sphere(pos0, pos1, radius=earth_rad):
    xyz0, xyz1 = latlng_to_xyz(*pos0), latlng_to_xyz(*pos1)
    try:

        distance = acos(sum(x * y for x, y in zip(xyz0, xyz1))) * radius
    except ValueError:
        return 0

    return distance


def get_distance(gps1, gps2):
    return dist_on_sphere(gps1, gps2)
