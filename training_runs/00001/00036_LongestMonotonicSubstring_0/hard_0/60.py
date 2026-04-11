def sat(x: List[int], length=13, s="Dynamic programming solves this puzzle!!!"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] >= 0 for i in range(length - 1))

def sol():
    x = [1, 2, 0, 10, 7, 12, 4, 6, 8, 11, 3, 5, 9]
    return x

if __name__ == "__main__":
    assert sat(sol())
