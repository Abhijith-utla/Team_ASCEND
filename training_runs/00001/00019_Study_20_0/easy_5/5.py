def sat(li: List[int]) -> bool:
    return all(li[i] <= li[i + 1] for i in range(len(li) - 1)) and li[0] <= li[-1]

def sol() -> int:
    return 0

def sat(li: List[int]) -> bool:
    return all(li[i] <= li[i + 1] for i in range(len(li) - 1)) and li[0] <= li[-1]

# Let's check the correctness of the solution
assert sat([1, 2, 3, 4])
assert not sat([1, 2, 4, 3])

if __name__ == "__main__":
    assert sat(sol())
