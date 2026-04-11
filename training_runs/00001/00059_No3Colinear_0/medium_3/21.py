def sat(coords: List[Tuple[int, int]], side=10, num_points=20):
    for (x1, y1), (x2, y2) in itertools.combinations(coords, 2):
        assert x1 * (y2 - y1) != 0
    return len(coords) >= num_points

def sol():
    return []

assert sat([])
assert not sat([(1,1)])
assert not sat([(1,1),(2,2)])
assert sat([(1,1),(2,2),(3,3)])
assert not sat([(1,1),(2,2),(3,3),(4,4)])
assert not sat([(1,1),(2,2),(3,3),(4,4),(5,5)])
assert sat([(1,1),(2,2),(3,3),(4,4),(5,5),(6,6)])
assert not sat([(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7)])
assert sat([(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8)])
assert not sat([(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9)])
assert

if __name__ == "__main__":
    assert sat(sol())
