def sat(coords: List[List[int]], side=2, num_points=1):
    for i in range(len(coords)):
        x, y = coords[i]
        assert x == y
    return len({(a, b) for a, b in coords}) == len(coords) >= num_points

def sol():
    return []

# Test case
assert sat([[0, 0]]) == True
assert sat([[0, 1], [1, 1]]) == True
assert sat([[0, 1], [2, 1]]) == False
assert sat([[0, 0]], side=3, num_points=2) == True
assert sat([[0, 1], [1, 2]], side=3, num_points=2) == False

if __name__ == "__main__":
    assert sat(sol())
