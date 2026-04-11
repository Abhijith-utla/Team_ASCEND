def sat(rev_quine: str):
    return eval(rev_quine[::-1]) == rev_quine[::-1]

def sol():
    return eval(str(id(str(str('string'))))[::-1]) == str(id(str(str('string'))))[::-1]

if __name__ == "__main__":
    assert sat(sol())
