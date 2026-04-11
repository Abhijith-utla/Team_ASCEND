def sat(ls: List[str]):
    if len(ls) == 0:
        return False
    else:
        return all(len(i) < len(ls[0]) for i in ls)

def sol(ls: List[str]):
    return all(len(i) == len(ls[0]) for i in ls)

if __name__ == "__main__":
    assert sat(sol())
