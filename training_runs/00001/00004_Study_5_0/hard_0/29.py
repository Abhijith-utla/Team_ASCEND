def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)])

def sol():
    from typing import List
    from collections import Counter
    c = Counter(range(10))
    return all([c[i] == i for i in range(10)])

# Test
print(sat(list(range(10))))  # True
print(sat(list(range(9)) + list(range(10))))  # False

if __name__ == "__main__":
    assert sat(sol())
