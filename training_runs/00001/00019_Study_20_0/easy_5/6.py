def sat(li: List[int]) -> bool:
    return all(li[i] <= li[i + 1] for i in range(len(li) - 1)) and li[0] <= li[-1]

def sol():
    return sat([4, 2, 3, 6])

# test case 1
assert sol() == True

# test case 2
assert sol() == False

# test case 3
assert sol() == True

# test case 4
assert sol() == False

# test case 5
assert sol() == True

# test case 6
assert sol() == False

# test case 7
assert sol() == True

# test case 8
assert sol() == False

# test case 9
assert sol() == True

# test case 10
assert sol() == False

if __name__ == "__main__":
    assert sat(sol())
