def sat(quine):
    return eval("print(" + quine + "); print('Hello, World!')")

def sol():
    return eval("print('Hello, World!')")

if __name__ == "__main__":
    assert sat(sol())
