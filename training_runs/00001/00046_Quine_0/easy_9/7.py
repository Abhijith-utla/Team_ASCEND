def sat(quine):
    return eval(quine + "()")()

def sol():
    return 42

if __name__ == "__main__":
    assert sat(sol())
