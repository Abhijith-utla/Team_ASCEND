def sat(rev_quine: str):
    return eval(rev_quine[::-1]) == rev_quine[0]

def sol():
    return "dneurf"

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
