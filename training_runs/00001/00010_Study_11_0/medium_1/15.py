def sat(ls: List[str]):
    if len(ls) == 0:
        return True
    else:
        return all(i in ls for i in range(len(ls)))

def sol(ls: List[str]):
    if len(ls) == 0:
        return True
    else:
        for i in range(len(ls)):
            if i not in ls:
                return False
        return True

if __name__ == "__main__":
    assert sat(sol())
