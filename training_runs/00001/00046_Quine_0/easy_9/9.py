def sat(quine):
    return eval(quine + "()")()

def sol():
    return None

# Testing the function
assert sat(sol)() == None

if __name__ == "__main__":
    assert sat(sol())
