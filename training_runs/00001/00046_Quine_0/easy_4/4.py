def sat(quine):
    return eval("print(" + quine + ")")

def sol():
    return ""

# This is for the checker to see if the solution works
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
