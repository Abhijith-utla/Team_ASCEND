def sat(x: int, y: int) -> bool:
    return x <= y

def sol():
    return {"answer": 1}

assert sat(sol()["answer"])

if __name__ == "__main__":
    assert sat(sol())
