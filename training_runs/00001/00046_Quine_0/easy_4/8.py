def sat(quine):
    return eval("print(" + quine + ")")

def sol():
    return "print(\"Hello, World!\")"

if __name__ == "__main__":
    assert sat(sol())
