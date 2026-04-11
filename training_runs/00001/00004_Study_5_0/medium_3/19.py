def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)]) and li.count(0) == 1

def sol(li: List[int]):
    return all([li.count(i) == i for i in range(10)]) and li.count(0) == 1

# For testing
li = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(sat(li))  # should print: True

li = [1, 2, 2, 3, 3, 3, 4, 4, 4, 5]
print(sat(li))  # should print: False

li = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(sat(li))  # should print: True

if __name__ == "__main__":
    assert sat(sol())
