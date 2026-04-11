def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

# Test case
print(sat(["a", "b", "c"]))  # True
print(sat(["a", "b", "c", "d"]))  # False
print(sat(["a"]))  # True
print(sat([]))  # False

if __name__ == "__main__":
    assert sat(sol())
