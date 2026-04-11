def sat(ls: List[str]):
    if len(ls) == 0:
        return True
    else:
        return all(len(i) == len(ls[0]) for i in ls)

def sol(ls: List[str]):
    if len(ls) == 0:
        return True
    else:
        return all(len(i) == len(ls[0]) for i in ls)

# Test cases
print(sol([]))  # True
print(sol(["abc", "def", "ghijk"]))  # False
print(sol(["abcdefg", "hij", "klmnop"]))  # True

if __name__ == "__main__":
    assert sat(sol())
