def sat(n: int):
    return lace[n:n + len(lace) // 2] == 'r' * (2 * n + 1)

def sol():
    return 0

# The output must be valid Python code only.

if __name__ == "__main__":
    assert sat(sol())
