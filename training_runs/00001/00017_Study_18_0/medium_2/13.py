def sat(ls: List[str]) -> bool:
    return all(len(set(s)) == len(s) for s in ls)

def sol():
    return len(set(input())) == 1

# Test cases
print(sat(["hello"]))  # True
print(sat(["hello", "world"]))  # False
print(sat(["aaaa", "bbbb", "cccc"]))  # True
print(sat(["1234", "4321", "7895"]))  # True

if __name__ == "__main__":
    assert sat(sol())
