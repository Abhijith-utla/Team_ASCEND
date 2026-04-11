def sat(rev_quine: str):
    return eval(rev_quine[::-1]) == rev_quine

def sol():
    return ""

# The solution will be checked by the checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
