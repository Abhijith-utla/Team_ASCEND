def sat(ls: List[str]) -> bool:
    return all(len(set(s)) == len(s) for s in ls)

def sol():
    return { "result": sat(['abc', 'bca', 'abcde']) }

if __name__ == "__main__":
    assert sat(sol())
