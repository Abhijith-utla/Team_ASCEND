def sat(quine: str):
    return eval(quine) == quine

def sol():
    return {}

print(eval(repr(sol())))

if __name__ == "__main__":
    assert sat(sol())
