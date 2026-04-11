def sat(x: List[int], length=13, s="Dynamic programming solves this puzzle!!!"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] >= 0 for i in range(length - 1))

def sol():
    return [1, 5, 8, 12, 16, 20, 23, 26, 29, 31, 33, 35, 37]

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
