def sat(rev_quine: str):
    return eval(rev_quine[::-1]) == rev_quine

def sol():
    return ""

# The following lines are to make the solution executable
if __name__ == "__main__":
    print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
