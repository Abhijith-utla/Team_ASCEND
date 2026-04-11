def sat(x: List[int], length=1, s="O!A{SeKv"):
    return all(s.count(s[x[i]]) == s.count(s[x[i + 1]]) for i in range(length - 1))

def sol():
    return [0, 1]

if __name__ == "__main__":
    assert sat(sol())
