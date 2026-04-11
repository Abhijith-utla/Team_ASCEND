def sat(li: List[int]):
    return sorted(li) == list(range(999))

def sol():
    return [i for i in range(1, 1000)]

# Check
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
