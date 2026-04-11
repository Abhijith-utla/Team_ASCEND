def sat(quine: str):
    return eval(quine) == quine

def sol():
    return ""

# Testing
quine = "print('Hello, World!')"
assert sat(quine)

if __name__ == "__main__":
    assert sat(sol())
