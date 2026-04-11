def sat(x: List[int], length=13, s="Dynamic programming solves this puzzle!!!"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] >= 0 for i in range(length - 1))

def sol():
    return [5, 3, 1, 6, 7, 8, 9, 4, 2, 0, 10, 11, 12]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
