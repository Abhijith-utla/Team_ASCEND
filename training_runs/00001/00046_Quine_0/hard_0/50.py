def sat(quine: str):
    return eval(quine) == quine

def sol():
    return None

if __name__ == "__main__":
    assert sat(sol())
