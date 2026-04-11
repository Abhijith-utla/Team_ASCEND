def sat(rev_quine: str):
    return eval(rev_quine) == rev_quine

def sol():
    return ""

# Test the solution
rev_quine = 'def sol():\n    return ""'
assert sat(rev_quine)

if __name__ == "__main__":
    assert sat(sol())
