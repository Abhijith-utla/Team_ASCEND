def sat(ls: List[int]):
    if len(ls) == 0:
        return True
    else:
        return all(i in ls for i in range(len(ls)))

def sol():
    return True

if __name__ == "__main__":
    assert sat(sol())
