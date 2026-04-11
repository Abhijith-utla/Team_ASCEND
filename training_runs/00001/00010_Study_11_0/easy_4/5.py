def sat(ls: List[str]):
    if len(ls) == 0:
        return False
    else:
        return all(len(i) == len(ls[0]) for i in ls)

def sol():
    return []

# Testing the function
assert sat(sol())

# Testing the function with an empty list
assert not sat([])

# Testing the function with a list of different length
assert not sat(['hello', 'hi'])

# Testing the function with a list of equal length
assert sat(['hello', 'hello'])

if __name__ == "__main__":
    assert sat(sol())
