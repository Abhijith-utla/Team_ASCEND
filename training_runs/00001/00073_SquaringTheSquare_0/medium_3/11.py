def sat(xy_sides):
    max_sum = max(x + side for x, y, side in xy_sides)
    assert len({side for x, y, side in xy_sides}) == len(xy_sides) > 1
    for x, y, s in xy_sides:
        assert 0 <= x and 0 <= y < max_sum and y + s <= max_sum and 0 <= s
        for x2, y2, s2 in xy_sides:
            assert s2 <= s or x2 >= x + s or x2 + s2 <= x or y2 >= y + s or y2 + s2 <= y
    return sum(side ** 2 for x, y, side in xy_sides) == max_sum ** 2

def sol():
    return [0, 0, 0]

# Test cases
print(sat([[0, 0, 0]])) # Returns [0, 0, 0]
print(sat([[5, 5, 1]])) # Returns [0, 0, 1]
print(sat([[5, 5, 5]])) # Returns [1, 1, 5]
print(sat([[10, 10, 5]])) # Returns [10, 10, 10]

# This test case will return [11, 11, 11] because the maximum sum is 11, and each side of the triangle has to be less than or equal to 11
print(sat([[10, 10, 11]])) 

# This test case will return [2, 2, 2] because the maximum sum is 2, and each side of the triangle is 2
print(sat([[2, 2, 1]])) 

# This test case will return [4,

if __name__ == "__main__":
    assert sat(sol())
