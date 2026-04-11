def sat(quine):
    return eval("print(" + quine + "); print('Hello, World!')")

def sol():
    return eval("print('Hello, World!')")

# Ensure the solution runs without errors
assert sat(str(sol()))

if __name__ == "__main__":
    assert sat(sol())
