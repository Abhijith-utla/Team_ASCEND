def sat(quine):
    return eval(quine + "()")

def sol():
    return None

# assert sat(sol)
!sat(sol)

if __name__ == "__main__":
    assert sat(sol())
