def sat(quine):
    return eval(quine + "()")

def sol():
    return None

def test():
    assert sat(sol)

test()

if __name__ == "__main__":
    assert sat(sol())
