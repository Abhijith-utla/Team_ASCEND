def sat(xy_sides):
    max_sum = max([x + side for x, y, side in xy_sides])

def sol():
    return [max(x + side for x, y, side in xy_sides)]

if __name__ == "__main__":
    assert sat(sol())
