from opsk.main import get_approximate_state_vectors, Coord, filter_by_radius, Result


def test_get_approximate_state_vectors():
    lat_min_max = (1, 2)
    lon_min_max = (3, 4)
    states = [Coord(latitude=1, longitude=3),
              Coord(latitude=1, longitude=1),
              Coord(latitude=3, longitude=5)]
    res = get_approximate_state_vectors(states, lat_min_max, lon_min_max)
    assert len(res) == 1


def test_filter_by_radius():
    radius = 100  # 1 degree is equal to approximately 100 km
    from_coord = Coord(1, 1)
    to_coords = [Result(1, 1, 'a'), Result(4, 4, 'b'), Result(1.5, 1.5, 'c')]
    res = filter_by_radius(radius, from_coord, to_coords)
    assert len(res) == 2
