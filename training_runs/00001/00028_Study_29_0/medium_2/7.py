def sat(l: list):
    return all(i in range(1000) and abs(i * i - j * j) < 10 for i in l for j in l if i != j)

def sol():
    l = [i for i in range(1000)]
    return l

# Assertion check
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
