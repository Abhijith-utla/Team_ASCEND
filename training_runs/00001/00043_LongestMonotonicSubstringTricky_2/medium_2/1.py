def sat(x: List[int], length=1, s="O!A{SeKv"):
    return all(s[x[i]] <= s[x[i + 1]] for i in range(length))

def sol():
    return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if __name__ == "__main__":
    assert sat(sol())
