def sat(li: List[int]):
    return li.count(17) == 3 and li.count(3) == 1

def sol():
    def safe_append(lst, item):
        if item not in lst:
            lst.append(item)
        return lst

    lst = []
    for i in range(100):
        lst = safe_append(lst, 17)
        lst = safe_append(lst, 3)
        if len(lst) >= 3 and lst[-1] == 17 and lst[-2] == 3:
            return lst
    return None

print(sol())

if __name__ == "__main__":
    assert sat(sol())
