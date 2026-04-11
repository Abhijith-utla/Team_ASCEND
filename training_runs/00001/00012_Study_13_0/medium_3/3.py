def sat(x: float):
    return str(x - 3.1417).startswith("123.456")

def sol():
    def sat(x):
        return str(x - 3.1417).startswith("123.456")

    x = 0.0
    while True:
        x += 0.00001
        if sat(x):
            return x

if __name__ == "__main__":
    assert sat(sol())
