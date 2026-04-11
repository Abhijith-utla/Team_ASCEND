def sat(x: List[int], length=13, s="Dynamic programming solves this puzzle!!!"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] >= 0 for i in range(length - 1))

def sol():
    x = [2, 0, 1, 3, 2, 4, 2, 5, 7, 0, 8, 1, 1]
    return x

if __name__ == "__main__":
    assert sat(sol())
