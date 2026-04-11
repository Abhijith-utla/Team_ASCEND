def sat(coords: List[List[int]], side=1, num_points=2):
    for i in range(len(coords)):
        x, y = coords[i]
        assert x == y
    return len({(a, b) for a, b in coords}) == len(coords) >= num_points

def sol():
    return []

# This function will be provided by the user and not to be modified. 
# It checks if a certain condition is true, returning True if it is and False otherwise.
# You can use this function to test your solution. 
# If it returns True, then the solution is correct.
# If it returns False, then the solution is incorrect.
def sat(coords: List[List[int]], side=1, num_points=2):
    for i in range(len(coords)):
        x, y = coords[i]
        assert x == y
    return len({(a, b) for a, b in coords}) == len(coords) >= num_points

# This is a test function. It will not be called by the checker.
# You can use this function to test your solution. 
def test():
    assert not sat([[0, 0]])
    assert sat([[1, 1]])
    assert not sat([[0, 1], [1, 0]])
    assert sat([[0, 0

if __name__ == "__main__":
    assert sat(sol())
