def sat(coords: List[List[int]], side=2, num_points=1):
    for i in range(len(coords)):
        x, y = coords[i]
        assert x == y
    return len({(a, b) for a, b in coords}) == len(coords) >= num_points

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
