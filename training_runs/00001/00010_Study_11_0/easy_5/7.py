def sat(ls: List[str]):
    if len(ls) == 0:
        return True
    else:
        return all(len(i) > len(ls[0]) for i in ls)

def sol():
    return [i for i in range(1, 11) if len(str(i)) > len(str(10))]

if __name__ == "__main__":
    assert sat(sol())
