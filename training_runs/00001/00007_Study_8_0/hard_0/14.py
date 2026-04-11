def sat(ls: List[str]):
    return ls[1234] in ls[1235] and ls[1234] != ls[1235]

def sol(ls: List[str]):
    if len(ls) < 13:
        return False
    for i in range(12):
        if ls[i] in ls[i+1:]:
            return False
    return True

def sat(ls: List[str]):
    return sol(ls)

if __name__ == "__main__":
    assert sat(sol())
