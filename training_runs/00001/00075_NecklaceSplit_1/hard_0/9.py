def sat(n: int, lace="rbbrrbbrbrbbbrrrbbrbrbrrbbrbbbbbbrrrrrrrrbrrrbbrbrrbbbrbbrrrbbrbbrrbrrbrbbrbbbbbbrbbbrbrbrrbrbbrbrrbbrrbrrbrrbrrbrbrbrrrbbrbrbbrrbbbbrrrrrbbrbrbrrbr"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return ""

# print(sat(0))
# print(sat(1))
# print(sat(2))
# print(sat(3))
# print(sat(4))
# print(sat(5))
# print(sat(6))
# print(sat(7))
# print(sat(8))
# print(sat(9))
# print(sat(10))
# print(sat(11))
# print(sat(12))
# print(sat(13))
# print(sat(14))
# print(sat(15))
# print(sat(16))
# print(sat(17))
# print(sat(18))
# print(sat(19))
# print(sat(20))
# print(sat(21))
# print(sat(22))
# print(sat(23))
# print(sat(24))
# print(sat(25))
# print(sat(26))
# print(sat(27))
# print(sat(

if __name__ == "__main__":
    assert sat(sol())
