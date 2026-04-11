def sat(x: List[int], l: int, s: str):
    return all(s[x[i]] <= s[x[i + 1]] for i in range(l - 1))

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())
