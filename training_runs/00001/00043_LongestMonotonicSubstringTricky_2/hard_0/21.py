def sat(x: List[int], length=1, s="O!A{SeKv"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] for i in range(length - 1))

def sol():
    return [0]

if __name__ == "__main__":
    assert sat(sol())
