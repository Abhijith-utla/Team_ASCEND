def sat(rev_quine: str):
    return eval(rev_quine[::-1]) == rev_quine[0]

def sol():
    return rev_quine[::-1]

if __name__ == "__main__":
    assert sat(sol())
