def sat(l: list):
    return all(i in range(996) for i in l if abs(i * i - j * j) >= 10)

def sol():
    for j in range(100):
        if all(i in range(996) for i in [(j*j + k*k) for k in range(1000)] if abs(i * i - j * j) >= 10):
            return j
    return -1

# test
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
