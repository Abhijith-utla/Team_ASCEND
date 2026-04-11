def sat(s: str) -> bool:
    if s == 'abc4.5':
        return True
    else:
        return False

def sol():
    return 'abc4.5'

if __name__ == "__main__":
    assert sat(sol())
