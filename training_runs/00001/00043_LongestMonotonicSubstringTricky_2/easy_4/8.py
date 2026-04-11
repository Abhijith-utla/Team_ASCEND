def sat(x: List[int]):
    return all(ord(ch) <= ord(s[x[i]]) for i in range(len(x)))

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())
