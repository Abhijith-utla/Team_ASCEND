def sat(x: List[int], l: int, s: str):
    return all(s[i] <= s[i + 1] for i in range(l))

def sol():
    return [1]

if __name__ == "__main__":
    assert sat(sol())
