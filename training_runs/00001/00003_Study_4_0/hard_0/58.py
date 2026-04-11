def sat(li: List[int]):
    return len(li) == 10 and li.count(li[3]) == 2

def sol():
    return [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
