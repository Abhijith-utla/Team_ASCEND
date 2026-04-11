def sat(x: List[int], length=20, s="Dynamic programming solves this classic job-interview puzzle!!!"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] for i in range(length - 1))

def sol():
    return [1, 2, 0, 3, 2, 4, 5, 7, 8, 6, 4, 3, 2, 1, 0, 5, 6, 7, 8, 9]

if __name__ == "__main__":
    assert sat(sol())
