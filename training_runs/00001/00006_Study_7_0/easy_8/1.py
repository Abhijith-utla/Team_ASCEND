def sat(s: str):
    return str(8 ** 2888).count(s) > 8 and len(s) == 3

def sol():
    for i in range(10**8):
        if str(8 ** 2888).count(str(i)) > 8 and len(str(i)) == 3:
            return i
    return None

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
