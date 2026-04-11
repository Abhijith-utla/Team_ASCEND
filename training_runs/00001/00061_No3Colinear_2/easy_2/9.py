def sat(coords: List[List[int]], side=1, num_points=1):
    for i in range(len(coords)):
        x, y = coords[i]
        assert x >= 0 and x < side
        assert y >= 0 and y < side
    return len({(a+1, b) for a, b in coords}) == len(coords) >= num_points

def sol():
    return []

# This function is not used in the solution, it's just a placeholder.
def not_used(coords, side=1, num_points=1):
    return []

# This function is not used in the solution, it's just a placeholder.
def not_used2(coords, side=1, num_points=1):
    return []

# This function is not used in the solution, it's just a placeholder.
def not_used3(coords, side=1, num_points=1):
    return []

# This function is not used in the solution, it's just a placeholder.
def not_used4(coords, side=1, num_points=1):
    return []

# This function is not used in the solution, it's just a placeholder.
def not_used5(coords, side=1, num_points=1):
    return []

# This function is not used in the solution, it's just a placeholder.
def not_used6(coords, side=1, num_

if __name__ == "__main__":
    assert sat(sol())
