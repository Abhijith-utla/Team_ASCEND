def sat(x: List[int], length=13, s="Dynamic programming solves this puzzle!!!"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] >= 0 for i in range(length - 1))

def sol():
    x = [3, 0, 2, 1, 5, 4, 6, 7, 9, 8, 10, 11, 12]
    length = len(x)
    s = "Dynamic programming solves this puzzle!!!"
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] >= 0 for i in range(length - 1))

if __name__ == "__main__":
    assert sat(sol())
