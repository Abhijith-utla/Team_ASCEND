def sat(l: list):
    return all(i in range(996) for i in l for j in l if abs(i * i - j * j) >= 10)

def sol():
    return [i, j]

# Test
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
