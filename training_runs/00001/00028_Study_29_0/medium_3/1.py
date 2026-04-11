def sat(l: list):
    return all(i in range(996) and abs(i * i - j * j) >= 10 for i in l for j in l if i != j)

def sol():
    l = []
    for i in range(996):
        for j in range(996):
            if abs(i * i - j * j) >= 10:
                l.append(i)
    return l

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
