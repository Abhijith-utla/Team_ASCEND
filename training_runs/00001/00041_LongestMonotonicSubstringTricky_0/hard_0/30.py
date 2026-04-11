def sat(x: List[int], length=20, s="Dynamic programming solves this classic job-interview puzzle!!!"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] for i in range(length - 1))

def sol():
    x = [i for i in range(20)]
    x[0] = 5
    x[1] = 3
    x[2] = 6
    x[3] = 2
    x[4] = 1
    x[5] = 7
    x[6] = 8
    x[7] = 0
    x[8] = 4
    x[9] = 10
    x[10] = 12
    x[11] = 13
    x[12] = 14
    x[13] = 15
    x[14] = 11
    x[15] = 9
    x[16] = 16
    x[17] = 17
    x[18] = 18
    x[19] = 19
    return x

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
