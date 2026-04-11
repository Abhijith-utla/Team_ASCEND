def sat(x: List[int], length=20, s="Dynamic programming solves this classic job-interview puzzle!!!"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] for i in range(length - 1))

def sol():
    return [1, 2, 3, 4, 5]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
