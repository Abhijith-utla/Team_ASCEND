def sat(xy_sides):
    max_sum = max([x + side for x, y, side in xy_sides])

def sol():
    return [max(x + side for x, y, side in xy_sides)]

xy_sides = [[3, 4, 5], [1, -2, 4], [-1, 2, 3]]
print(sat(xy_sides))

if __name__ == "__main__":
    assert sat(sol())
