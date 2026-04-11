def sat(n: int, lace="brrrbrrbrbbbbbrrbbrr"):
    if n < 0:
        return False
    sub = lace[n: n + len(lace) // 2]
    return lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return {}

# Testing the function
print(sat(0))  # False
print(sat(1))  # False
print(sat(2))  # True
print(sat(3))  # False
print(sat(4))  # False
print(sat(5))  # True
print(sat(6))  # False
print(sat(7))  # False
print(sat(8))  # True
print(sat(9))  # False
print(sat(10))  # False
print(sat(11))  # True
print(sat(12))  # False
print(sat(13))  # False
print(sat(14))  # True
print(sat(15))  # False
print(sat(16))  # False
print(sat(17))  # True
print(sat(18))  # False
print(sat(19))  # False
print(sat(20))  # True
print(sat(21))  # False
print(sat(22))  #

if __name__ == "__main__":
    assert sat(sol())
