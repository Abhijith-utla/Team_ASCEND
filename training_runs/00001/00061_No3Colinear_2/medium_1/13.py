def sat(coords: List[List[int]], side=1, num_points=1):
    for i in range(len(coords)):
        x, y = coords[i]
        assert x >= 0 and x < side
        assert y >= 0 and y < side
    return len({(a, b) for a, b in coords}) == len(coords) >= num_points

def sol():
    return []

# Test cases
print(sat([[0, 0], [0, 1], [1, 1]], 2, 3))  # True
print(sat([[0, 0], [0, 1], [1, 0]], 2, 3))  # False
print(sat([[0, 0], [0, 1], [1, 1]], 2, 2))  # True
print(sat([[0, 0], [0, 1], [1, 0]], 2, 4))  # False

if __name__ == "__main__":
    assert sat(sol())
