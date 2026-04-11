def sat(x: List[int], length=13, s="Dynamic programming solves this puzzle!!!"):
    return len(x) >= length

def sol():
    return []

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
