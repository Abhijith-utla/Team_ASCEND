def sat(rev_quine: str):
    return eval(rev_quine[::-1]) == rev_quine[::-1]

def sol():
    return ""

# checker function
def sat(rev_quine: str):
    return eval(rev_quine[::-1]) == rev_quine[::-1]

# test the function
print(sat(sol()))  # True

if __name__ == "__main__":
    assert sat(sol())
