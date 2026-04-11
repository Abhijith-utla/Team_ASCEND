def sat(xy_sides):
    max_sum = max([x + side for x, y, side in xy_sides])
    return sum([side for x, y, side in xy_sides]) == max_sum

def sol():
    return [max(0, x + y) for x, y, side in xy_sides]

print(sol())

print(sat([])) # False
print(sat([(1, 2, 3), (1, 2, 3), (1, 2, 3)])) # False
print(sat([(1, 1, 1), (1, 2, 3), (1, 2, 3)])) # True

if __name__ == "__main__":
    assert sat(sol())
