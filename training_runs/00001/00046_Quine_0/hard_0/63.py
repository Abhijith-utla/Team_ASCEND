def sat(quine: str):
    return eval(quine) == quine

def sol():
    return ""

# This test ensures the quine is a valid python code
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
