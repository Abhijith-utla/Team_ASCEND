def sat(x: List[int], s="O!A{SeKv"):
    return all(ord(ch) <= ord(s[x[i]]) for i in range(len(x)))

def sol():
    x = [0]
    s = "O!A{SeKv"
    return x, s

if __name__ == "__main__":
    assert sat(sol())
