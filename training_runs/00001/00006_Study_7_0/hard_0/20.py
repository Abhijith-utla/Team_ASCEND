def sat(s: str):
    return str(8 ** 2888).count(s) > 8 and len(s) == 3

def sol():
    for s in range(10):
        if str(8 ** 2888).count(str(s)) > 8 and len(str(s)) == 3:
            return s
    return -1

print(sol())

if __name__ == "__main__":
    assert sat(sol())
