def sat(coords: List[Tuple[int, int]], side=10, num_points=20):
    for i, (x1, y1) in enumerate(coords):
        assert 0 <= x1 < side and 0 <= y1 < side
    return len(coords) > num_points

def sol():
    return []

print(sat([]))
print(sat([(0, 0)]))
print(sat([(0, 0)] * 19))
print(sat([(0, 0)] * 20))
print(sat([(0, 0)] * 100))

if __name__ == "__main__":
    assert sat(sol())
