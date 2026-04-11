def sat(xy_sides):
    assert len(xy_sides) >= 2
    max_sum = max([x + side for x, y, side in xy_sides])
    return sum([side ** 2 for x, y, side in xy_sides]) == max_sum ** 2

def sol():
    return [0, 0, 0]

# Check the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
