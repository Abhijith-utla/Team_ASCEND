def sat(li: List[int]):
    return sorted(li) == list(range(len(li))) and all(li[i] != i for i in range(len(li))) and len(li) == 1000

def sol():
    return sorted(list(range(1000)))

# Test
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
