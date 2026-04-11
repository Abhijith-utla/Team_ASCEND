def sat(li: List[int]):
    return li.count(1) == 1 and li.count(2) == 1 and li.count(3) == 1 and li.count(4) == 1 and li.count(5) == 1 and li.count(6) == 1 and li.count(7) == 1 and li.count(8) == 1 and li.count(9) == 1

def sol():
    return 1

# Checker
def test_sat():
    import inspect
    import random
    from typing import List
    li: List[int] = [random.randint(1, 9) for _ in range(7)]
    li.append(random.randint(1, 9))
    assert sat(li) == (li.count(1) == 1 and li.count(2) == 1 and li.count(3) == 1 and li.count(4) == 1 and li.count(5) == 1 and li.count(6) == 1 and li.count(7) == 1 and li.count(8) == 1 and li.count(9) == 1)
    print('All tests passed.')

test_sat()

if __name__ == "__main__":
    assert sat(sol())
