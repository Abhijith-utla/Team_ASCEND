def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    return str(len(ls))

assert sat([str(len(ls)) for ls in [min(ls) for ls in [max(ls) for ls in range(10)]]])

if __name__ == "__main__":
    assert sat(sol())
