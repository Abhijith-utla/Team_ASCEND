def sat(rev_quine: str):
    return eval(rev_quine[::-1]) == rev_quine

def sol():
    return ""

def sat(rev_quine: str):
    return eval(rev_quine[::-1]) == rev_quine

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
