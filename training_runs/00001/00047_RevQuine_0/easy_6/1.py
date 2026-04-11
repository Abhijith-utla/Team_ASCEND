def sat(quine: str):
    return eval(quine[::-1]) == quine

def sol():
    return eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval

if __name__ == "__main__":
    assert sat(sol())
