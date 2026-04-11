def sat(n: int):
    s = str(n * n)
    return len(set(s)) == 10

def sol():
    return 1234567890

print(sat(sol()))  # True

print(sat(sol()))  # False

if __name__ == "__main__":
    assert sat(sol())
