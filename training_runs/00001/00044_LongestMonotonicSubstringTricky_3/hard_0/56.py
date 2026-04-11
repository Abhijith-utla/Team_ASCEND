def sat(x: List[int], length=61, s=" OW##P%T'UW)X+X-YY]^_`bd/044e5egk7lm779:<m?D@ADnnpDEFIpNNOqqwxx"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] for i in range(length - 1))

def sol():
    return []

# Test cases
assert sat([])
assert not sat([0])
assert sat([1, 0])
assert not sat([0, 1])
assert sat([0, 1, 2])
assert not sat([2, 1, 0])
assert sat([0, 1, 2, 3, 4, 5])
assert not sat([5, 4, 3, 2, 1, 0])
assert sat([0, 1, 2, 3, 4, 5, 6])
assert not sat([6, 5, 4, 3, 2, 1, 0])
assert sat([0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14

if __name__ == "__main__":
    assert sat(sol())
