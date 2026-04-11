def sat(quine):
    return eval("print(" + quine + ")")

def sol():
    return "Hello, world!"

if __name__ == "__main__":
    assert sat(sol())
