def sat(l: List[int]):
    return all(i in range(1000) and abs(i * i - j * j) >= 10 for i in l for j in l if i != j) and len(set(l)) > 995

def sol():
    return []

# Test case 1
# The list contains numbers 1-995, all perfect squares apart from 991, which are 9 and 81.
# Therefore, all(i in range(1000) and abs(i * i - j * j) >= 10 for i in l for j in l if i != j) will return False.
def test_case_1():
    l = list(range(1, 996))
    assert not sat(l)

# Test case 2
# The list contains numbers 1-995, all perfect squares apart from 991, which are 9, 81 and 169.
# Therefore, all(i in range(1000) and abs(i * i - j * j) >= 10 for i in l for j in l if i != j) will return True.
def test_case_2():
    l = list(range(1, 1000))
    assert sat(l)

# Test case 3
# The

if __name__ == "__main__":
    assert sat(sol())
