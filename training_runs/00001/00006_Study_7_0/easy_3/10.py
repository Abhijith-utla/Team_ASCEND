def sat(s: str):
    return str(int(8 ** 2888)).count(s) == 10 and len(s) == 3

def sol():
    # Create a string of characters to be found in the number
    s = '8' * 10 ** 6
    return s

if __name__ == "__main__":
    assert sat(sol())
