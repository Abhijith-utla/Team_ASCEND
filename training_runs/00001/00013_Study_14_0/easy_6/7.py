def sat(li: List[int]):
    return all(li.index(x) < sum(li[:i]) for i in range(len(li)) for x in set(li))

def sol():
    def sat(li: List[int]):
        return all(li.index(x) < sum(li[:i]) for i in range(len(li)) for x in set(li))

    return sat([])

# Test case
assert sol() == False
assert sol([1, 2, 3, 4, 5]) == True
assert sol([1, 1, 3, 4, 5]) == False
assert sol([5, 4, 3, 2, 1]) == True
assert sol([1, 2, 3, 5, 6]) == False

if __name__ == "__main__":
    assert sat(sol())
