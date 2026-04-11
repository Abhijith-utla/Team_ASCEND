def sat(coords: List[Tuple[int, int]], side=10, num_points=20):
    for i, (x, y) in enumerate(coords):
        assert 0 <= x < side and 0 <= y < side
    return len(coords) == num_points-1

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
