def sat(x: List[int], s: str):
    return all(s[i] <= s[i + 1] for i in range(len(x) - 1))

def sol():
    x = [1, 2, 3, 4, 5]
    s = 'abcd'
    assert sat(x, s)
    return x, s

if __name__ == "__main__":
    assert sat(sol())
