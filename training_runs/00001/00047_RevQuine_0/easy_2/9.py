def sat(rev_quine: str):
    return eval(rev_quine) == rev_quine

def sol():
    return ""

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
