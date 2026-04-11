def sat(coords: List[List[int]], side=1, num_points=2):
    for i in range(len(coords)):
        x, y = coords[i]
        assert x == y
    return len({(a, b) for a, b in coords}) == len(coords) >= num_points

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())
