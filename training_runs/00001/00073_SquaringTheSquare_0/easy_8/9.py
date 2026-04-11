def sat(xy_sides):
    max_sum = max([x + side for x, y, side in xy_sides])
    return sum([side for x, y, side in xy_sides]) == max_sum

def sol():
    return [0, 0, 0]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
