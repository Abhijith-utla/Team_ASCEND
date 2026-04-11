def sat(nums: List[int]):
    return [sorted([int(s) for s in str(n * n)]) for n in set(nums)] == [list(range(10))] * 174

def sol():
    return [int(s) for s in sorted(str(n * n))]

# Checker:
assert sat([int(s) for s in sorted(str(n * n))] for n in range(10))

if __name__ == "__main__":
    assert sat(sol())
