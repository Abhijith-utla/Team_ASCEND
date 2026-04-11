def sat(s: str):
    if s.count('oo') != 0:
        return False
    return True

def sol():
    return 'oo' if not sat() else ''

def sat(s: str):
    if s.count('oo') != 0:
        return False
    return True

if __name__ == "__main__":
    assert sat(sol())
