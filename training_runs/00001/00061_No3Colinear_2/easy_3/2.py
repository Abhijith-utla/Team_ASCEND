def sat(coords: List[List[int]], side=1, num_points=1):
    for i in range(len(coords)):
        x, y = coords[i]
        assert x >= 0 and x < side
        assert y >= 0 and y < side
    return len({(a, b+1) for a, b in coords}) == len(coords) >= num_points

def sol():
    return []

# The test case
print(sat([[0,0],[1,1],[2,2]])) # should return True
print(sat([[0,0],[1,1],[2,2]], side=3)) # should return True
print(sat([[0,0],[1,1],[2,2]], num_points=2)) # should return False
print(sat([[0,0],[1,1],[2,2]], side=3, num_points=2)) # should return False

if __name__ == "__main__":
    assert sat(sol())
