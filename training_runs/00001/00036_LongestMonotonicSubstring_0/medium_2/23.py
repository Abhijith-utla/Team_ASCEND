def sat(x: List[int], length=13, s="Dynamic programming solves this puzzle!!!"):
    # Check if the list is not empty
    # Also check if the list contains at least one substring in sorted order
    # Check if there are two adjacent elements which are increasing but in reversed order
    return len(x) > 0 and any(s[x[i]] <= s[x[i + 1]] for i in range(length - 1)) and any(x[i] < x[i + 1] for i in range(length - 1))

def sol():
    return [4, 3, 2, 1, 12, 11, 10, 9, 8, 7, 6, 5, 0]

if __name__ == "__main__":
    assert sat(sol())
