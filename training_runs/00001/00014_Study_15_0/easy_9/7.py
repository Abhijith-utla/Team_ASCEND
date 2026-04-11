def sat(li: List[int]):
    return all(x == sum(li[:i]) for i in range(1, len(li) + 1))

def sol():
    return sat

# The assertion will pass if the function sol is defined correctly.
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
