def sat(li: List[int]):
    return all([li.count(i) == i for i in range(1, 11)])

def sol():
    from collections import Counter
    li = list(map(int, input().split()))
    count = Counter(li)
    return all([count[i] == i for i in range(1, 11)])

if __name__ == "__main__":
    assert sat(sol())
