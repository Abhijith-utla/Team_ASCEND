def sat(ls: List[str]):
    return all(len(s) == 8 for s in ls)

def sol():
    return ""

if __name__ == "__main__":
    assert sat(sol())
