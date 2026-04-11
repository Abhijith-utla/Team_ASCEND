def sat(coords: List[Tuple[int, int]], side=10, num_points=20):
    for i, (x, y) in enumerate(coords):
        assert 0 <= x < side and 0 <= y < side
    return len(coords) == num_points-1

def sol():
    return []

# Assuming that the function sat is already defined and it takes a list of tuples and returns a boolean
# and that the function sol is defined such that it takes no arguments and returns a list of integers
# Since the problem does not specify a way to generate the coordinates, I'm using a simple list of integers as an example

def test_sol():
    assert len(sol()) == 0
    coords = [(0, 0), (5, 5), (10, 10)]
    assert sat(coords)
    coords = [(0, 0), (5, 5), (11, 10)]
    assert not sat(coords)
    coords = [(0, 0), (5, 5), (10, 11)]
    assert not sat(coords)

test_sol()

if __name__ == "__main__":
    assert sat(sol())
