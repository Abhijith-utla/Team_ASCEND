def sat(n: int):
    return lace[n:n + len(lace) // 2] == 'r' * (2 * n)

def sol():
    return ''

# Insert your code here. Replace the code in brackets with the correct Python code to solve this problem.

if __name__ == "__main__":
    assert sat(sol())
