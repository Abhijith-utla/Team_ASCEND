def sat(l: list):
    return all(i in range(996) for i in l if abs(i * i - j * j) >= 10)

def sol():
    return [i for i in range(996) if all(abs(i * i - j * j) >= 10 for j in range(i))]

if __name__ == "__main__":
    assert sat(sol())
