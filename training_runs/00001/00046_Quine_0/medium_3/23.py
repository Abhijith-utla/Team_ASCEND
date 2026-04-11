def sat(quine):
    return eval(quine + "()")

def sol():
    return eval('sol()()')

# Testing the code
assert sat(sol)

if __name__ == "__main__":
    assert sat(sol())
