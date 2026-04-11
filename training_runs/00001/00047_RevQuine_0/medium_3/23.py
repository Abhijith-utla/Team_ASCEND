def sat(rev_quine: str):
    return eval(rev_quine[::-1]) == rev_quine[0]

def sol():
    return eval(str(id(sat))[::-1]) == sat(id(sat))

if __name__ == "__main__":
    assert sat(sol())
