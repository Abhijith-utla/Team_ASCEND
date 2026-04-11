def sat(quine):
    return eval("print((" + quine + "))")

def sol():
    return ""

# Assertion for the question's solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
