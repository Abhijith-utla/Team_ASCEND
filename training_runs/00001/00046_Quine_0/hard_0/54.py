def sat(quine: str):
    return eval(quine) == quine

def sol():
    return ''

# Test the function
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
