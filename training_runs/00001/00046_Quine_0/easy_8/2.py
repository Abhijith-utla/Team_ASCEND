def sat(quine):
    return eval(quine + "()")

def sol():
    return None

# Testing the correctness of the solution
assert sat(sol)

if __name__ == "__main__":
    assert sat(sol())
