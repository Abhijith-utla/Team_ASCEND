def sat(ls: List[str]):
    if len(ls) == 0:
        return True
    else:
        return all(len(i) == len(ls[0]) for i in ls)

def sol():
    return ["python", "programming", "puzzle"]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
