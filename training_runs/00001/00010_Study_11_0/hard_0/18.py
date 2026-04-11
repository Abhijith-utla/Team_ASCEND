def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    return len(max(min(sat(ls) for ls in itertools.permutations(range(10)))))

def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
