def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    n = len(ls)
    return [i for i in range(n)]

if __name__ == "__main__":
    assert sat(sol())
