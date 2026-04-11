def sat(x: List[int], length=13, s="Dynamic programming solves this puzzle!!!"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] >= 0 for i in range(length - 1))

def sol():
    x = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    return x

if __name__ == "__main__":
    assert sat(sol())
