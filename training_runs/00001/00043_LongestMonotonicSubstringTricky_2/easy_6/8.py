def sat(x: List[int], s="O!A{SeKv"):
    return all(ord(ch) <= ord(s[x[i]]) for i in range(len(x)))

def sol():
    return [0]

if __name__ == "__main__":
    assert sat(sol())
