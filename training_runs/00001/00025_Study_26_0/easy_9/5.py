def sat(ls: List[str]):
    return "".join(ls) == '123456789' and all(len(s) == 9 for s in ls)

def sol():
    return [i for i in '123456789' if i in ''.join(i for i in range(1,10))]

if __name__ == "__main__":
    assert sat(sol())
