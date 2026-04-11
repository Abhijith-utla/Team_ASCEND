def sat(quine):
    return eval("print(" + quine + ")")

def sol():
    return 'Hello, World!'

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
