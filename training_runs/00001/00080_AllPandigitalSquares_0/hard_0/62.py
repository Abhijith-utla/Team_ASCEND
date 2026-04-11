def sat(nums: List[int]):
    return [sorted([int(s) for s in str(n * n)]) for n in set(nums)] == [list(range(10))] * 174

def sol():
    return [int(s) for s in sorted(str(i * i) * 174) if int(s) != 0]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
