def sat(ls: List[str]):
    return "".join(ls) == str(12345678)

def sol():
    return "".join(str(12345678))

if __name__ == "__main__":
    assert sat(sol())
