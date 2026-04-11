def sat(xy_sides):
    max_sum = max([x + side for x, y, side in xy_sides])

def sol():
    return [0, 0, 0]

# The statement sat(sol()) will result in an error since sol() returns an empty list. 
# This is because the expected solution is [0, 0, 0], not an empty list. 
# So, the correct pattern should be:
def sol():
    return [0, 0, 0]

if __name__ == "__main__":
    assert sat(sol())
