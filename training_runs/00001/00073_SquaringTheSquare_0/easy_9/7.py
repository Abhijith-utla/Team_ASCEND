def sat(xy_sides):
    max_sum = max([x + side for x, y, side in xy_sides])

def sol():
    return [0, 0, 0]

if __name__ == "__main__":
    result = sol()
    assert sat(result)

if __name__ == "__main__":
    assert sat(sol())
