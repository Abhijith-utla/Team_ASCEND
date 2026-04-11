def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)-1))

def sol():
    return [i for i in range(999) if i not in [li[i] for li in [sorted(list(range(999)))]]]

# Test
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
