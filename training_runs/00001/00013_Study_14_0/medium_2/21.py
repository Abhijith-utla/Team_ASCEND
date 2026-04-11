def sat(li: List[int]):
    return all([i < li.index(x) + sum(li[:li.index(x)]) for x in set(li)])

def sol():
    return {
        "result": all([i < li.index(x) + sum(li[:li.index(x)]) for x in set(li)])
    }

# Test cases
assert sat([3, 2, 1, 4, 6]) == True
assert sol() == {"result": True}
assert sat([1, 2, 3, 4, 5]) == False
assert sol() == {"result": False}

if __name__ == "__main__":
    assert sat(sol())
