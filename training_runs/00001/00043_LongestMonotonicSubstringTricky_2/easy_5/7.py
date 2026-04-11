def sat(x: List[int], length=1, s="O!A{SeKv"):
    return all(ord(ch) <= ord(s[x[i]]) for i in range(length))

def sol():
    return [0]

if __name__ == "__main__":
    assert sat(sol())
