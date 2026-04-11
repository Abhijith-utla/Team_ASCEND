def sat(n: int):
    return n % 2 == 0

def sol():
    return {"answer": True} if sat(0) else {"answer": False}

if __name__ == "__main__":
    assert sat(sol())
