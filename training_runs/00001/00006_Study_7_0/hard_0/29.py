def sat(s: str):
    return str(8 ** 2888).count(s) > 8 and len(s) == 3

def sol():
    def sat(s: str):
        return str(8 ** 2888).count(s) > 8 and len(s) == 3

    n = 0
    while not sat(str(n)):
        n += 1

    return n

if __name__ == "__main__":
    assert sat(sol())
