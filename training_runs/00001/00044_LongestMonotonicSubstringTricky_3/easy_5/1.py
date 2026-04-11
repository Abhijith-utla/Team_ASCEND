def sat(x: List[int], y: List[int]) -> bool:
    return all(x[i] <= y[i] for i in range(len(x)))

def sol():
    return []

# This function does not have any inputs so it does not take any
# It returns an empty list
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
