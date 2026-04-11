def sat(coords, side=1, num_points=1):
    for i in range(len(coords)):
        x, y = coords[i]
        assert 0 <= x < side
        assert 0 <= y < side
    return len({(a, b) for a, b in coords}) == len(coords) - num_points

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
