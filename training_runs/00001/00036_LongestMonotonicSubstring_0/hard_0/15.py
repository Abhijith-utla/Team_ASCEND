def sat(x: List[int], length=13, s="Dynamic programming solves this puzzle!!!"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] >= 0 for i in range(length - 1))

def sol():
    return [1, 3, 2, 4, 0, 5, 7, 6, 8, 9, 10, 11, 12]

if __name__ == "__main__":
    assert sat(sol())
