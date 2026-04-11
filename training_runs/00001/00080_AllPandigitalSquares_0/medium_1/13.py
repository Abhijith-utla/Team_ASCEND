def sat(nums: List[int]):
    return sorted([int(str(n) + str(n*n)) for n in nums]) == list(range(1, 10))

def sol():
    return [1, 4, 9]

# Correct pattern:
# def sol():
#     return [1, 4, 9]

# Incorrect pattern:
# def sol(x):
#     ...

# assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
