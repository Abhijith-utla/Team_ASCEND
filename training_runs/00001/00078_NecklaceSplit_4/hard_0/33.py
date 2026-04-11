def sat(n: int, lace="brrbbbrbbrrbrrbbrrbrrrbbrbbrrrbrbrbrrrrbbrrrbrrbbbbrbbbrrbbrrrbbrbrbbbbbrrbrrbbr"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return 5

# To pass the test, you can change the value of `n`
# For example, if you want to test the function with `n=4`, you can do it like this:
# assert sat(4)
# assert sat(5)
# assert not sat(6)

if __name__ == "__main__":
    assert sat(sol())
