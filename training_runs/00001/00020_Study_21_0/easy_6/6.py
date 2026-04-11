def sat(li: List[int]):
    return all(li[i] != li[i + 1] for i in range(8) if len(set(li)) == 3)

def sol():
    return 1

# Testing
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
