def sat(quine: str):
    return eval(quine) == quine

def sol():
    return eval("1 + 1")

if __name__ == "__main__":
    assert sat(sol())
