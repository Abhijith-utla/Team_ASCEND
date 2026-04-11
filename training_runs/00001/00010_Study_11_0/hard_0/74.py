def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    return min(str(i) for i in range(10)) == max(str(i) for i in range(10)) == str(len(range(10)))

if __name__ == "__main__":
    assert sat(sol())
