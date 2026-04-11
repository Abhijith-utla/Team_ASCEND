def sat(expr: str):
    digits = ""
    for i in range(len(expr)):
        if expr[i] in "123456789":
            digits += expr[i]
    assert sorted(int(s) for s in digits.split()) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "Each number must occur exactly once"
    return eval(expr) == 24.0

def sol():
    return "973846521"

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
