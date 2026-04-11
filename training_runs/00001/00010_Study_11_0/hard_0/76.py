def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    return len(set(str(i) for i in range(1, 11))) == 1

print(sat(str(i) for i in range(1, 11)))

if __name__ == "__main__":
    assert sat(sol())
