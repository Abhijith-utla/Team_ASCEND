def sat(quine):
    return eval("print((" + quine + "))")

def sol():
    return eval("print((" + quine() + "))")

if __name__ == "__main__":
    assert sat(sol())
