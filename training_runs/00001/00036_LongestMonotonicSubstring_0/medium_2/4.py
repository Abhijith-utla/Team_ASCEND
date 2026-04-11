def sat(x: List[int], length=13, s="Dynamic programming solves this puzzle!!!"):
    # Check if the list is not empty
    # Also check if the list contains at least one substring in sorted order
    # Check if there are two adjacent elements which are increasing but in reversed order
    return len(x) > 0 and any(s[x[i]] <= s[x[i + 1]] for i in range(length - 1)) and any(x[i] < x[i + 1] for i in range(length - 1))

def sol():
    x = [i for i in range(13)]
    x[12] = 0
    x[11] = 1
    x[10] = 2
    x[9] = 3
    x[8] = 4
    x[7] = 5
    x[6] = 6
    x[5] = 7
    x[4] = 8
    x[3] = 9
    x[2] = 10
    x[1] = 11
    x[0] = 12
    return x

print(sol())

if __name__ == "__main__":
    assert sat(sol())
