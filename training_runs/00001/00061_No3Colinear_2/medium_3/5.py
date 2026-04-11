def sat(coords: List[List[int]], side=1, num_points=1):
    for i in range(len(coords)):
        x, y = coords[i]
        assert x == y
    return len({(a, b) for a, b in coords}) == len(coords) >= num_points

def sol():
    return []

# To ensure the function `sol` returns a list, it needs to be called with some arguments.
# But since `sol` doesn't take any arguments, it will return an empty list.

if __name__ == "__main__":
    assert sat(sol())
