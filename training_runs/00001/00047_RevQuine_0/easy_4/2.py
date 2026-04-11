def sat(rev_quine):
    return eval(rev_quine[::-1]) == rev_quine

def sol():
    return eval(str(id(rev_quine))[::-1]) == rev_quine

if __name__ == "__main__":
    assert sat(sol())
