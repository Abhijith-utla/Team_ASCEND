def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10, 0, -1)])

def sol():
    return [i for i in range(10, 0, -1) if [li.count(i) for li in range(10, 0, -1)] == i]

# This is an assertion to check the correctness of the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
