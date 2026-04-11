def sat(n: int, lace="bbbbrrbbbbrrbbrrrbbrrbbrrrrrrrbrbrbbbrrbrrrbbbbbbbbbrbrbrbbbbbbbrrbbrbbrbrrbrbrrbbbrrrrrbrrbbrrrbbrbrrrbbbbrbbbrrrrbrbrrbbrbrbrbbrrbrrrbrbrrbbbbbbrbrrrrbbrbbbbbrrrbrbbr"):
    return lace[n - 1:n + len(lace) // 2] == 'r' * (2 * (n - 1))

def sol():
    return 'r' * 100000

# Test case
assert sat(1, 'bbbbrrbbbbrrbbrrrbbrrbbrrrrrrrbrbrbbbrrbrrrbbbbbbbbbrbrbrbbbbbbbrrbbrbbrbrrbrbrrbbbrrrrrbrrbbrrrbbrbrrrbbbbrbbbrrrrbrbrrbbrbrbrbbrrbrrrbrbrrbbbbbbrrrrbbrbbbbbbbrrrbrbbr')

# Do not modify anything below this line

# Checking function with test case
assert sat(2, 'bbbbrrbbbbrrbbrrrbbrrbbrrrrrrrbrbrbbbrrbrrrbbbbbbbbbrbrbrbbbbbbbrrbbrbbrbrrbrbrrbbbrrrrrbrrbbrrrbbrbrrrbbbbrbbbrrrrbrbrrbbrbrbrbbrrbrrrbrbrrbbbbbbrrrrbbrbbbbbbbrrrbrbbr')

if __name__ == "__main__":
    assert sat(sol())
