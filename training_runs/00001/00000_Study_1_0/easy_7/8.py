def sat(s: str):
    if s.count('o') != 1000:
        return False
    return True

def sol():
    return "A string with 1000 'o' characters."

if __name__ == "__main__":
    assert sat(sol())
