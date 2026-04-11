def sat(x: List[int], l: int, s: str):
    return all(s[i] <= s[i + 1] for i in x)

def sol():
    return []

# Assertions
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
