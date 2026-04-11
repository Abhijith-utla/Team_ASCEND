def sat(coords: List[List[int]], side=1, num_points=1):
    for i in range(len(coords)):
        x, y = coords[i]
        assert 0 <= x < side
        assert 0 <= y < side
    return len({(a, b) for a, b in coords}) == len(coords) >= num_points

def sol():
    return []

assert sat([])
assert not sat([[0, 0]])
assert not sat([[0, 0], [0, 1]])
assert sat([[0, 0], [1, 0]])
assert not sat([[0, 0], [0, 1], [1, 1]])
assert not sat([[0, 0], [0, 1], [1, 0]])
assert not sat([[0, 0], [0, 1], [2, 1]])
assert not sat([[0, 0], [0, 1], [1, 0], [1, 1]])
assert not sat([[0, 0], [0, 1], [1, 0], [2, 0]])
assert sat([[0, 0], [0, 1], [1, 0], [2, 1]])
assert not sat([[0, 0], [0, 1], [1, 0], [1, 1], [3, 2

if __name__ == "__main__":
    assert sat(sol())
