def sat(rev_quine: str):
    return eval(rev_quine[::-1]) == rev_quine

def sol():
    return eval(str(id(str(__builtins__.input))))

if __name__ == "__main__":
    assert sat(sol())
