def sat(rev_quine: str):
    return eval(rev_quine) == rev_quine.strip()

def sol():
    return ''

# Testing
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
