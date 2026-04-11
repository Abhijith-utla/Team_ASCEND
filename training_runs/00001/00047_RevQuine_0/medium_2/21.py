def sat(rev_quine: str):
    return eval(rev_quine[::-1]) == rev_quine[::-1]

def sol():
    return eval(str(id(sat)))

if __name__ == "__main__":
    assert sat(sol())
