def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    return len(set(str(x) for x in range(10))) == 1

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
