from geopy.geocoders import Nominatim


def get_coord(*args):
    """Gets latitude and longitude from args through geopy.geocoders.Nominatim.

    Returns
    -------
    tuple
        A tuple (lat, long) with latitude and longitude
    """

    maps_args = ", ".join(tuple(map(str, filter(lambda x: x is not None, args))))

    geoloc = Nominatim(user_agent="test_app")

    return geoloc.geocode(maps_args)
