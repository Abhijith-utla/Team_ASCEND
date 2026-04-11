def sat(rev_quine: str):
    return eval(rev_quine[::-1]) == rev_quine

def sol():
    return rev_quine == rev_quine[::-1]

if __name__ == "__main__":
    assert sat(sol())
