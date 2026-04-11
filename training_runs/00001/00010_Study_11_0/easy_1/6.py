def sat(ls: List[int]):
    if len(ls) == 0:
        return True
    else:
        return all(i in ls for i in range(len(ls)))

def sol():
    return False

def sat(ls: List[int]):
    if len(ls) == 0:
        return True
    else:
        return all(i in ls for i in range(len(ls)))

if __name__ == "__main__":
    assert sat(sol())
