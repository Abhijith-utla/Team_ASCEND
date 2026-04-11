def sat(rev_quine: str):
    return eval(rev_quine) == rev_quine

def sol():
    return ""

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
