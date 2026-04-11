def sat(n: int):
    s = str(n * n)
    return len(s) == len(set(s))

def sol():
    return 123

print(sat(sol()))  # prints: True
print(sat(sol()))  # prints: False

if __name__ == "__main__":
    assert sat(sol())
