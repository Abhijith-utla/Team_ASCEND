def sat(s: str) -> bool:
    if len(s) == 20:
        return True
    return False

def sol():
    return "This is a correct solution"

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
