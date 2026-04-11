def sat(x: List[int], length=13, s="Dynamic programming solves this puzzle!!!"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] >= 0 for i in range(length - 1))

def sol():
    return [2, 1, 4, 3, 6, 5, 9, 0, 8, 7, 11, 10, 13]

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
