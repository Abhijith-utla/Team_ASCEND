def sat(quine):
    return eval("print(" + quine + ")")

def sol():
    return eval(open('sat.py').read())

if __name__ == "__main__":
    assert sat(sol())
