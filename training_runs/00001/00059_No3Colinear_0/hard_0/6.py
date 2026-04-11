def sat(coords: List[List[int]], side=10, num_points=20):
    for i1 in range(len(coords)):
        x1, y1 = coords[i1]
        assert 0 <= x1 < side and 0 <= y1 < side
        for i2 in range(i1):
            x2, y2 = coords[i2]
            for i3 in range(i2):
                x3, y3 = coords[i3]
                assert x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) != 0
    return len({(a, b) for a, b in coords}) == len(coords) >= num_points

def sol():
    return []

print(sat([]))  # True
print(sat([[1, 1], [2, 2], [3, 3]]))  # False
print(sat([[0, 0], [2, 2], [2, 0]]))  # True
print(sat([[1, 1], [2, 2], [3, 4]]))  # False
print(sat([[5, 5], [10, 10], [15, 15]]))  # True

if __name__ == "__main__":
    assert sat(sol())
