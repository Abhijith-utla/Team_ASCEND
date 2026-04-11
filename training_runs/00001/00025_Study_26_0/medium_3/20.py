def sat(ls: List[str]):
    return "".join(ls) == str(987654321) and all(len(s) == 8 for s in ls)

def sol():
    return [str(i) for i in range(10)]

if __name__ == "__main__":
    assert sat(sol())
