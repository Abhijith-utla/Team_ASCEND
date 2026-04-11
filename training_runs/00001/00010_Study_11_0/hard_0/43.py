def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    return len(min(ls)) == len(max(ls)) == len(ls)

if __name__ == "__main__":
    assert sat(sol())
