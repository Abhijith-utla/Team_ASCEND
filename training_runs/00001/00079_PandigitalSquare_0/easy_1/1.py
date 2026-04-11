def sat(n: int):
    s = str(n * n)
    return set(s) == {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

def sol():
    return 123456789

if __name__ == "__main__":
    assert sat(sol())
