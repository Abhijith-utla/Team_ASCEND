def sat(l: list):
    return all(i in range(996) and abs(i * i - j * j) >= 10 for i in l for j in l if i != j)

def sol():
    l = [x for x in range(996)]
    return l

# Checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
