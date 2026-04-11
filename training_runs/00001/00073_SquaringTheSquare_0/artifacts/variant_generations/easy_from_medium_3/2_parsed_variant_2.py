def sat(xy_sides):
    max_sum = max([x + side for x, y, side in xy_sides])
    return sum([side for x, y, side in xy_sides]) == max_sum

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
