def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    number_string = str(8 ** 1818)
    return sat(number_string)

print(sol())

if __name__ == "__main__":
    assert sat(sol())
