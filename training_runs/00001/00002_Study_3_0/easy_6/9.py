def sat(li: List[int]) -> bool:
    return sorted(li) == list(range(999)) and all(li[i] == i for i in range(len(li)))

def sol():
    return [i for i in range(999) if i not in [li[i] for li in [i for i in range(999)]]]

# Test
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
