def sat(li: List[int]):
    return len(li) == 10 and max(li) == 12

def sol() -> int:
    return 12

def sat(li: List[int]):
    return len(li) == 10 and max(li) == 12

# Test
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
