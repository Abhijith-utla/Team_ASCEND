def sat(li: List[int]) -> bool:
    if len(li) != 10:
        return False
    if li.count(li[3]) != 2:
        return False
    return True

def sol():
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return li

# Checker
def sat(li: List[int]) -> bool:
    if len(li) != 10:
        return False
    if li.count(li[3]) != 2:
        return False
    return True

# Run the checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
