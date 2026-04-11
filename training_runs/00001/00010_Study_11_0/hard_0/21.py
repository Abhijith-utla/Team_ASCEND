def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    return Answer(sat(["1", "2", "3", "4", "5"]))

def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

if __name__ == "__main__":
    assert sat(sol())
