def sat(li: List[int]):
    return li.count(17) == 3 and li.count(3) >= 2

def sol():
    # This solution assumes that the function 'sat' is provided by the user and that the function 'count' is a built-in Python function.
    # If these assumptions are not valid, this solution may not work as expected.
    li = [3, 3, 3, 17, 17, 17, 17, 1, 1, 1, 1, 1, 1, 1]
    li.sort()
    cnt1 = 0
    cnt3 = 0
    for i in li:
        if i == 17:
            cnt1 += 1
        if i == 3:
            cnt3 += 1
    if cnt1 == 3 and cnt3 >= 2:
        return True
    else:
        return False

if __name__ == "__main__":
    assert sat(sol())
