def sat(quine):
    return eval(quine + "()")()

def sol():
    return 'Hello, World!'

# Test
assert sat(sol) == 'Hello, World!'

if __name__ == "__main__":
    assert sat(sol())
