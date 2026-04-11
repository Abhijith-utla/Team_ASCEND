def sat(x: List[int], length=1, s="xwV"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] >= 0 for i in range(length - 1))

def sol():
    return [0, 1, 2, 3]

if __name__ == "__main__":
    assert sat(sol())
