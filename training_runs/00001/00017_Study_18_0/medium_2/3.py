def sat(ls: List[str]) -> bool:
    return all(len(set(s)) == len(s) for s in ls)

def sol():
    def sat(ls: List[str]) -> bool:
        return all(len(set(s)) == len(s) for s in ls)
    
    assert sat(["abc", "bcd", "efg"])
    assert not sat(["abcd", "bcd", "efg"])
    assert not sat(["abc", "bcd", "ef"])
    assert sat(["a", "aa", "aaa"])
    assert not sat(["ab", "abc", "abcd"])
    return {}

if __name__ == "__main__":
    assert sat(sol())
