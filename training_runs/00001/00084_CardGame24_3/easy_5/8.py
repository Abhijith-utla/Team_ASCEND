def sat(expr: str):
    expr = expr.replace(" ", "")  # ignore whitespace
    digits = ""
    for i in range(len(expr)):
        if expr[i] in "123456789(*)":
            digits += expr[i] if expr[i] in "0123456789" else " "
    assert sorted(int(s) for s in digits.split()) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "Each number must occur exactly once"
    return eval(expr) == 25.0

def sol():
    return ""

if __name__ == "__main__":
    assert sat(sol())
