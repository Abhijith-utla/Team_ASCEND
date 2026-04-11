def sat(x: float):
    return str(x - 3.1415).startswith("123.456")

def sol():
    return {"answer": str(3.1415 - 3.1415)}

print(sol()["answer"])

if __name__ == "__main__":
    assert sat(sol())
