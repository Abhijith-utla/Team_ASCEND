def sat(coords: List[Tuple[int, int]], side=10, num_points=20):
    for (x1, y1), (x2, y2) in itertools.combinations(coords, 2):
        assert x1 * (y2 - y1) != 0
    return len(coords) >= num_points

def sol(coords: List[Tuple[int, int]], side=10, num_points=20):
    def cross_product(o, i, j):
        return (o[0] - i[0]) * (j[1] - o[1]) - (o[1] - i[1]) * (j[0]

if __name__ == "__main__":
    assert sat(sol())
