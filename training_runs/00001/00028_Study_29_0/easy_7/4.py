def sat(l: list):
    return all(i in range(996) for i in l if abs(i * i - j * j) >= 10 for j in l)

def sol():
    return [i for i in range(996) if abs(i * i - (j * j) * (j * j)) >= 10 for j in range(996)]

if __name__ == "__main__":
    assert sat(sol())
