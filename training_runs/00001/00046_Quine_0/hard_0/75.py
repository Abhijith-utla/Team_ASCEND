def sat(quine: str):
    return eval(quine) == quine

def sol():
    return eval(str(quine)) == quine

if __name__ == "__main__":
    assert sat(sol())
