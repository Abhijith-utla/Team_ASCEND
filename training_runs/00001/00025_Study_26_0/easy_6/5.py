def sat(ls: List[str]):
    return "".join(ls) == str(1234567890)

def sol():
    return "".join(str(1234567890))

if __name__ == "__main__":
    assert sat(sol())
