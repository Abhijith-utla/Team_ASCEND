def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)]) and li.count(0) == 1

def sol(li: List[int]):
    count = [li.count(i) for i in range(10)]
    if max(count) > 1 or min(count) < 2:
        return False
    zero_index = count.index(0)
    count[zero_index] = 1
    return all(li.count(i) == count[i] for i in range(10))

if __name__ == "__main__":
    assert sat(sol())
