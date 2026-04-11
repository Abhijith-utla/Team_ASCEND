def sat(s: str):
    if s.count('o') != 0:
        return False
    return True

def sol():
    return 'Success' if sat('') else 'Failure'

if __name__ == "__main__":
    assert sat(sol())
