def sat(coords: List[Tuple[int, int]], side=10, num_points=20):
    for i, (x1, y1) in enumerate(coords):
        assert 0 <= x1 < side and 0 <= y1 < side
    return len(coords) >= num_points

def sol():
    return []

print(sat([])) # returns True
print(sat([(5, 5)])) # returns False
print(sat([(5, 5)], side=10, num_points=20)) # returns True
print(sat([(5, 5)], side=10)) # returns False
print(sat([(5, 5)], num_points=20)) # returns True
print(sat([(5, 5)], side=10, num_points=200)) # returns False
print(sat([(5, 5), (6, 7), (8, 9)], side=10, num_points=20)) # returns True
print(sat([(5, 5), (6, 7), (8, 9)], side=10)) # returns False
print(sat([(5, 5), (6, 7), (8, 9)], num_points=200)) # returns False

if __name__ == "__main__":
    assert sat(sol())
