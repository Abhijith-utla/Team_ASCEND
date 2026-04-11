def sat(li: List[int]):
    return li.count(17) == 3 and li.count(3) == 0

def sol():
    li = [17, 3, 17, 17, 3]
    return li.count(17) == 3 and li.count(3) == 0

# Checker
def sat(li: List[int]):
    return li.count(17) == 3 and li.count(3) == 0

if __name__ == "__main__":
    assert sat(sol())
