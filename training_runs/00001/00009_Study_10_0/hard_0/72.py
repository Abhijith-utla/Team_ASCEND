def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    def check(s: str):
        return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

    def gen():
        s = ""
        for _ in range(12):
            s += str(8)
        return s

    s = gen()
    while not check(s):
        s = gen()

    return s

# Check the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
