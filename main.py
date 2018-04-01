from typing import Tuple, List
from collections import namedtuple

import geopy.distance
from opensky_api import OpenSkyApi, StateVector

api = OpenSkyApi()
Coord = namedtuple('Coord', ['latitude', 'longitude'])
Result = namedtuple('Result', ['latitude', 'longitude', 'callsign'])


def get_approximate_state_vectors(latitude_min_max: Tuple[int, int],
                                  longitude_min_max: Tuple[int, int]) -> List[StateVector]:
    '''
    To extract StateVectors from OpenSky about planes by LatLon limits.
    '''
    states = api.get_states().states
    res = []
    for s in states:
        if s.latitude and s.longitude:
            latitude_between_cond = (latitude_min_max[0] <= s.latitude <= latitude_min_max[1])
            longitude_between_cond = (longitude_min_max[0] <= s.longitude <= longitude_min_max[1])
            if latitude_between_cond and longitude_between_cond:
                res.append(s)
    return res


def filter_by_radius(radius_km: int, from_coord: Coord,
                     to_coords: List[StateVector]) -> List[Result]:
    '''
    Calculation is based on accurate Vincenty formula (approximation of 1mm).
    '''
    res = []
    for coord in to_coords:
        to_coord = (coord.latitude, coord.longitude)
        distance = geopy.distance.vincenty(from_coord, to_coord).km
        if distance <= radius_km:
            result = Result(callsign=coord.callsign, latitude=coord.latitude,
                            longitude=coord.longitude)
            res.append(result)
    return res


if __name__ == '__main__':
    # Get approximated results
    latitude_min_max = (38, 58)
    longitude_min_max = (-8, 12)
    vectors = get_approximate_state_vectors(latitude_min_max=latitude_min_max,
                                            longitude_min_max=longitude_min_max)
    # Get accurate results
    paris = Coord(latitude=48.864716, longitude=2.349014)
    radius_km = 450
    answer = filter_by_radius(radius_km=radius_km, from_coord=paris, to_coords=vectors)
    print(answer)
