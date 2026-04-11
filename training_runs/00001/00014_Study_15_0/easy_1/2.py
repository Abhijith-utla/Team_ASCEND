def sat(li: List[int]):
    return all(x >= 0 and 2 ** x - 1 == (2 ** x) - 1 for x in li)

def sol():
    return {
        'answer': 2 ** 10 - 1  # Make sure that the value is less than 2 ** 10, otherwise the result is incorrect
    }

# Testing the solution
assert sat([1, 2, 3, 4, 5])
assert not sat([1, -2, 3, 4, 5])
assert not sat([2, 3, 5, 7, 9])
assert sat([10, 100, 1000, 10000, 100000])

if __name__ == "__main__":
    assert sat(sol())
