def sat(s: str):
    if s.count('oo') != 0:
        return False
    return True

def sol():
    return 'oo'

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
