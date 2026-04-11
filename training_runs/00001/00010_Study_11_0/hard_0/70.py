def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    return [min(ls), max(ls)]

if __name__ == "__main__":
    assert sat(sol())
