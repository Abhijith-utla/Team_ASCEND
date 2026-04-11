def sat(quine: str):
    return eval(quine) == quine

def sol():
    return {}

# Tests
assert sat(str(sol()))
!python -c "print('sol()')"

if __name__ == "__main__":
    assert sat(sol())
