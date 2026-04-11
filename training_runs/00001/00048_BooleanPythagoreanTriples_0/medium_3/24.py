def sat(n: int, m: int, p: int):
    assert n >= 0, 'n must be greater than or equal to 0'
    assert m >= 0, 'm must be greater than or equal to 0'
    assert p >= 0, 'p must be greater than or equal to 0'
    assert n + m + p == m, 'Sum of n, m, and p must equal m'
    return n + m >= p

def sol():
    n = int(input("Enter a number n: "))
    m = int(input("Enter a number m: "))
    p = int(input("Enter a number p: "))
    return n, m, p

print("The sum of n, m, and p is:", sol())

if __name__ == "__main__":
    assert sat(sol())
