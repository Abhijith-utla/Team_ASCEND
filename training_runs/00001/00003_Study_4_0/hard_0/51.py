def sat(li: List[int]):
    return len(li) == 10 and li.count(li[3]) == 2

def sol():
    return [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

print(sat(sol()))

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
