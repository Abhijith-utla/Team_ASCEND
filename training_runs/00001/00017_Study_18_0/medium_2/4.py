def sat(ls: List[str]) -> bool:
    return all(len(set(s)) == len(s) for s in ls)

def sol():
    def sat(ls: List[str]) -> bool:
        return all(len(set(s)) == len(s) for s in ls)

    assert sat(["cat", "dog", "cat", "act"]) == False
    assert sat(["cat", "dog", "cat", "act", "dog"]) == True

    return None

if __name__ == "__main__":
    assert sat(sol())
