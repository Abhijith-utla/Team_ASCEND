def sat(xy_sides: List[List[int]]):
    n = max(x + side for x, y, side in xy_sides)
    assert len({side for x, y, side in xy_sides}) == len(xy_sides) > 1
    for x, y, s in xy_sides:
        assert 0 <= y < y + s <= n and 0 <= x
        for x2, y2, s2 in xy_sides:
            assert s2 <= s or x2 >= x + s or x2 + s2 <= x or y2 >= y + s or y2 + s2 <= y

    return sum(side ** 2 for x, y, side in xy_sides) == n ** 2

def sol():
    return [0, 0]

# This is to simulate the test case
# It is not a realistic situation, but it can be used to test the correctness of the solution
def sim(x, y, side):
    return [x, y, side]

# This is the main function, it generates random values and checks whether they are valid
def main():
    import random
    while True:
        x, y, side = [random.randint(0, 10) for _ in range(3)]
        xy_sides = [sim(x, y, side) for _ in range(4)]
        if sat(xy_sides):
            return [x, y]

print(main())

if __name__ == "__main__":
    assert sat(sol())
