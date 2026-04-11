def sat(quine):
    return eval(quine + "()")()

def sol():
    return eval("return " + "()")()

if __name__ == "__main__":
    assert sat(sol())
