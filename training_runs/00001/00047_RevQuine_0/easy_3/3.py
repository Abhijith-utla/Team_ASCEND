def sat(rev_quine: str):
    return eval(rev_quine) == rev_quine.strip()

def sol():
    return ""

def sat(rev_quine: str):
    return eval(rev_quine) == rev_quine.strip()

# Test
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
