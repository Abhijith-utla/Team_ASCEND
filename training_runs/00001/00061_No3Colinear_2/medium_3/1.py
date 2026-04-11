def sat(coords: List[List[int]], side=1, num_points=1):
    for i in range(len(coords)):
        x, y = coords[i]
        assert x == y
    return len({(a, b) for a, b in coords}) == len(coords) >= num_points

def sol():
    return []

assert sat([])
assert not sat([[1,1]])
assert not sat([[1,2],[2,1]])
assert sat([[1,1]], side=2, num_points=1)
assert not sat([[1,2],[2,1]], side=2, num_points=1)
assert sat([[1,1]], side=3, num_points=1)
assert not sat([[1,2],[2,1]], side=3, num_points=1)
assert not sat([[1,1]], side=1, num_points=2)
assert not sat([[1,2],[2,1]], side=1, num_points=2)
assert not sat([[1,1]], side=1, num_points=3)

if __name__ == "__main__":
    assert sat(sol())
