def sat(s: str):
    if s.count('o') != 1000:
        return False
    return True

def sol():
    return "1000"

if __name__ == "__main__":
    assert sat(sol())
