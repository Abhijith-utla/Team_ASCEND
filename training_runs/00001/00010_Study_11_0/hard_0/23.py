def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    return len(max(min(sat(str(int(input()))))))

def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

print(sol())

if __name__ == "__main__":
    assert sat(sol())
