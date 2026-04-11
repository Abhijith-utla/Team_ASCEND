def sat(rev_quine: str):
    return eval(rev_quine[::-1]) == rev_quine[::-1]

def sol():
    return ""

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
