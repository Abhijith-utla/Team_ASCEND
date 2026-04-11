def sat(coords: List[List[int]], side=1, num_points=1):
    for i in range(len(coords)):
        x, y = coords[i]
        assert x >= 0 and x < side
        assert y >= 0 and y < side
    return len({(a, b) for a, b in coords}) == len(coords) >= num_points

def sol():
    return []

# Example of how to use the solution
# print(sat([[1, 2], [2, 3], [3, 4]]))  # This will print False
# print(sat([[1, 2], [2, 3], [3, 3]]))  # This will print True

if __name__ == "__main__":
    assert sat(sol())
