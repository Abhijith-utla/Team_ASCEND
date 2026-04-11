def sat(coords: List[Tuple[int, int]], side=2, num_points=4):
    for i1, (x1, y1) in enumerate(coords):
        assert 0 <= x1 < side and 0 <= y1 < side
        if (x1, y1) in coords[:i1]:
            continue
        for x2, y2 in coords[i1+1:]:
            for x3, y3 in coords[i1+2:]:
                if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0:
                    return False
    return len(set(coords)) == num_points

def sol():
    return []

print(sat([(0, 0), (1, 1), (2, 2), (3, 3)]))  # Should return True
print(sat([(0, 0), (1, 1), (2, 2), (4, 4)]))  # Should return False
print(sat([(0, 0), (1, 0), (1, 1), (0, 2)]))  # Should return True
print(sat([(0, 0), (1, 0), (1, 1), (0, 2)], side=5, num_points=4))  # Should return False
print(sat([(0, 0), (1, 0), (1, 1), (0, 2)], side=3, num_points=3))  # Should return True

if __name__ == "__main__":
    assert sat(sol())
