def sat(coords: List[List[int]], side=1, num_points=2):
    for i in range(len(coords)):
        x, y = coords[i]
        assert x == y
    return len({(a, b) for a, b in coords}) == len(coords) >= num_points

def sol():
    return []

# Testing the solution
print(sat([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]])) # Should return False
print(sat([[1, 1], [2, 2], [3, 3], [4, 4]])) # Should return False
print(sat([[1, 1], [2, 2], [3, 3]])) # Should return True
print(sat([[1, 1], [2, 2]])) # Should return True
print(sat([[1, 1]])) # Should return True
print(sat([[1, 2]])) # Should return False

if __name__ == "__main__":
    assert sat(sol())
