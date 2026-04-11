def sat(quine):
    return eval(quine + "()")()

def sol():
    return 42

# check
assert sat(sol)() == 42

if __name__ == "__main__":
    assert sat(sol())
