def sat(x: List[int], length=20, s="Dynamic programming solves this classic job-interview puzzle!!!"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] for i in range(length - 1))

def sol():
    x = [i for i in range(20)]
    x[0] = 19
    x[19] = 1
    return x

if __name__ == "__main__":
    assert sat(sol())
