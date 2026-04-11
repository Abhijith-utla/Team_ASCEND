def sat(x: List[int], length: int, s: str):
    return all(s[x[i]] < s[x[i + 1]] for i in range(length - 1))

def sol():
    return []

print(sat([], 0, ""))
!python -m doctest -v < filename

if __name__ == "__main__":
    assert sat(sol())
