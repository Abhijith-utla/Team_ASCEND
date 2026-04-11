def sat(quine: str):
    return eval(quine) == quine

def sol():
    return eval('return ' + str(quine))

# Checker code
def sat(quine: str):
    return eval(quine) == quine

if __name__ == "__main__":
    assert sat(sol())
