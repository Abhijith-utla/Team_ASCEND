def sat(s: str) -> bool:
    if len(s) != 20:
        return False
    return True

def sol():
    return 'a'*20

if __name__ == "__main__":
    assert sat(sol())
