def sat(s: str):
    if s.count('o') != 0:
        return False
    return True

def sol():
    if 'o' in 'python':
        return False
    return True

if __name__ == "__main__":
    assert sat(sol())
