def sat(i: int):
    return i < 100

def sol():
    return {"answer": 12}

assert sat(sol()["answer"])

if __name__ == "__main__":
    assert sat(sol())
