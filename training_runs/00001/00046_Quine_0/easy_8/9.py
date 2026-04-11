def sat(quine):
    return eval(quine + "()")

def sol():
    return {}

# Testing the function
assert sat(sol)

if __name__ == "__main__":
    assert sat(sol())
