def sat(quine):
    return eval("print(" + quine + "); print('Hello, World!')")

def sol():
    return 'Hello, World!'

# Test
assert sat(repr(sol()))

if __name__ == "__main__":
    assert sat(sol())
