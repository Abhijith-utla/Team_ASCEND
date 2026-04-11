def sat(quine):
    return eval(quine[::-1]) == quine

def sol():
    return eval(str(quine)) == quine

if __name__ == "__main__":
    assert sat(sol())
