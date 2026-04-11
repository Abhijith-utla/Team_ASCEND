def sat(ls: List[str]) -> bool:
    return len(ls) == len(set(ls))

def sol(ls: List[str]) -> bool:
    return len(ls) == len(set(ls))

def test():
    assert sol(["apple", "banana", "apple"]) == False
    assert sol(["apple", "banana", "cherry"]) == True
    print("All tests passed")

test()

if __name__ == "__main__":
    assert sat(sol())
