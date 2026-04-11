def sat(rev_quine: str):
    return eval(rev_quine) == rev_quine

def sol():
    return ""

# Test
print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
