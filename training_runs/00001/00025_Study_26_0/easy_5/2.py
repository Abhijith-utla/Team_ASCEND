def sat(ls: List[str]):
    return "".join(ls) == str(123456789)

def sol():
    return ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

if __name__ == "__main__":
    assert sat(sol())
