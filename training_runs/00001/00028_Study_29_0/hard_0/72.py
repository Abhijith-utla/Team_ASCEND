def sat(l: List[int]):
    return all(i in range(1000) and abs(i * i - j * j) >= 10 for i in l for j in l if i != j) and len(set(l)) > 995

def sol():
    return []

# Assertion should be done manually in the main block
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
