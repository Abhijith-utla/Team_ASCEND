def sat(x: float):
    return str(x - 3.1416).startswith("123.456")

def sol():
    return {"answer": 123.456 - 3.1416}

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
