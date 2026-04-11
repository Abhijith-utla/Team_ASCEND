def sat(s: str):
    return str((8 ** 2888) ** 0.5).count(s) > 8 and len(s) == 3

def sol():
    return Answer(str((8 ** 2888) ** 0.5).count('3') > 8 and len(str((8 ** 2888) ** 0.5)) == 3)

if __name__ == "__main__":
    assert sat(sol())
