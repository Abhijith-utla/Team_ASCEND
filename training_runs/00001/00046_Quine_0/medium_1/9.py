def sat(quine):
    return eval(quine) == quine

def sol():
    return ''

if __name__ == "__main__":
    assert sat(sol())
