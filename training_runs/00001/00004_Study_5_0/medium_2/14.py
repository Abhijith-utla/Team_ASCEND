def sat(li: List[int]):
    return all([li.count(i) == i for i in range(1, 11)])

def sol():
    from collections import Counter
    counter = Counter([i for i in range(1, 11)])
    return counter == Counter()

if __name__ == "__main__":
    assert sat(sol())
