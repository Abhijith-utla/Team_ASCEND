def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    ls = [1, 2, 3, 4, 5]
    return sat(ls)

def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

if __name__ == "__main__":
    assert sat(sol())
