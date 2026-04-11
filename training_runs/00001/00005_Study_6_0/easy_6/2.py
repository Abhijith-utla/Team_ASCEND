def sat(i: int):
    return i % 5 == 0 and i < 100

def sol():
    for i in range(100):
        if i % 5 == 0 and i < 100:
            return i

if __name__ == "__main__":
    assert sat(sol())
