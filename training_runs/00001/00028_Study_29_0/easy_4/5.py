def sat(l: list):
    return all(i in range(1000) and abs(i * i - j * j) < 10 for i in l for j in l if i != j)

def sol():
    return [i for i in range(1000) for j in range(1000) if i != j and abs(i * i - j * j) < 10]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
