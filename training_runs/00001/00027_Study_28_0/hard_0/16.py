def sat(li: List[int]):
    return all(i in range(1000) and abs(i - j) >= 10 for i in li for j in li if i != j) and len(set(li)) == 100

def sol():
    return []

# Checker:
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
