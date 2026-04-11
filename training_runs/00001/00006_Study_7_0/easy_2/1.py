def sat(s: str):
    return str(int(8 ** 2888)).count(s) == 8 and len(s) == 5

def sol():
    s = '8765'
    while not sat(s):
        s += '65'
    return s

print(sol())

if __name__ == "__main__":
    assert sat(sol())
