def sat(coords: List[List[int]], side=1, num_points=2):
    for i in range(len(coords)):
        x, y = coords[i]
        assert x == y
    return len({(a, b) for a, b in coords}) == len(coords) >= num_points

def sol():
    return []

# This function will always return an empty list because the coords list is empty.

if __name__ == "__main__":
    assert sat(sol())
