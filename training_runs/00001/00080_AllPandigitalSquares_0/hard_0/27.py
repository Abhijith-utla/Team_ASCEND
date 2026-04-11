def sat(nums: List[int]):
    return [sorted([int(s) for s in str(n * n)]) for n in set(nums)] == [list(range(10))] * 174

def sol():
    return []

print(sat([123, 321, 456, 789, 987]))

if __name__ == "__main__":
    assert sat(sol())
