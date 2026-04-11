def sat(l: list):
    return all(i in range(996) for i in l if abs(i * i - j * j) >= 10)

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())
