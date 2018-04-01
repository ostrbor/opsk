from lib import api, get_approximate_state_vectors, Coord, filter_by_radius

if __name__ == '__main__':
    # Get approximated results
    states = api.get_states().states
    latitude_min_max = (38, 58)
    longitude_min_max = (-8, 12)
    vectors = get_approximate_state_vectors(states,
                                            latitude_min_max=latitude_min_max,
                                            longitude_min_max=longitude_min_max)
    # Get accurate results
    paris = Coord(latitude=48.864716, longitude=2.349014)
    radius_km = 450
    answer = filter_by_radius(radius_km=radius_km, from_coord=paris, to_coords=vectors)
    print(answer)
