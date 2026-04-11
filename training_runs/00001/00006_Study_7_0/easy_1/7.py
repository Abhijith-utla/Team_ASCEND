def sat(s: str):
    return str(int(8 ** 2888)).count(s) == 8 and len(s) == 3

def sol():
    i = 1
    while True:
        if len(str(i)) == 3:
            return i
        i += 1

if __name__ == "__main__":
    assert sat(sol())
