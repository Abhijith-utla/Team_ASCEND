def sat(quine):
    return eval(quine + "()")()

def sol():
    return None

# Test
assert sat(sol)() == None

if __name__ == "__main__":
    assert sat(sol())
