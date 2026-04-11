def sat(expr: str):
    digits = ""
    for i in range(len(expr)):
        if expr[i] in "123456789":
            digits += expr[i]
    assert sorted(int(s) for s in digits.split()) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "Each number must occur exactly once"
    return eval(expr) == 24.0

def sol():
    return eval(str(1) + "+" + str(2) + "+" + str(3) + "+" + str(4) + "+" + str(5) + "+" + str(6) + "+" + str(7) + "+" + str(8) + "+" + str(9) + "+" + str(10) + "/" + str(11) + "+" + str(12) + "+" + str(13) + "+" + str(14) + "+" + str(15) + "+" + str(16) + "+" + str(17) + "+" + str(18) + "+" + str(19) + "+" + str(20) + "/" + str(21) + "+" + str(22) + "+" + str(23) + "+" + str(24))

print(sol())

if __name__ == "__main__":
    assert sat(sol())
