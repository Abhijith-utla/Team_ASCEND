def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    ls = [str(i) for i in range(10)]  # Replace 0 to 9 to use the correct range.
    return min(ls) == max(ls) == str(len(ls))

if __name__ == "__main__":
    assert sat(sol())
