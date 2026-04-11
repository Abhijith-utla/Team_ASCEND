def sat(ls: List[str]) -> bool:
    return all(len(set(s)) == len(s) for s in ls)

def sol():
    def inner(ls: List[str]) -> bool:
        return all(len(set(s)) == len(s) for s in ls)
    return inner

if __name__ == "__main__":
    assert sat(sol())
