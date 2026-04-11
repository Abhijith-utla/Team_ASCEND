def sat(l: list):
    return all(i in range(996) and abs(i * i - j * j) >= 10 for i in l for j in l if i != j)

def sol():
    return [i for i in range(996) if all(abs(i * i - j * j) >= 10 for j in range(996) if i != j)]

if __name__ == "__main__":
    assert sat(sol())
