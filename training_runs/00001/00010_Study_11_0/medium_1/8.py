def sat(ls: List[str]):
    if len(ls) == 0:
        return True
    else:
        return all(i in ls for i in range(len(ls)))

def sol():
    return [i for i in range(len(list(range(1, 11)))) if i not in list(range(1, 11))]

if __name__ == "__main__":
    assert sat(sol())
