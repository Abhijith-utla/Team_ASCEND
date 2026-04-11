def sat(n: int, lace="bbbbrrbbbbrrbbrrrbbrrbbrrrrrrrbrbrbbbrrbrrrbbbbbbbbbrbrbrbbbbbbbrrbbrbbrbrrbrrbbbrrrrrbrrbbrrrbbrbrrrbbbbrbbbrrrrbrbrrbbrbrbrbbrrbrrrbrrrrbbbbbbrbrrrrbbrbbbbbrrrbrbbr"):
    return lace[:len(lace) // 2] == 'r' * (2 * n)

def sol():
    return 'r' * (2 * 1)

# The output is valid Python code only.
# Do not modify this line.
print(sol())

if __name__ == "__main__":
    assert sat(sol())
