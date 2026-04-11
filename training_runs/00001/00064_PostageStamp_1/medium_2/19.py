def sat(stamps: List[int], target=271, max_stamps=8, options=[1, 2, 3]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# Adding a stamp of value 1 to the stamps list
def sol1():
    return [1]

# Adding a stamp of value 2 to the stamps list
def sol2():
    return [1, 2]

# Adding a stamp of value 3 to the stamps list
def sol3():
    return [1, 2, 3]

# Adding a stamp of value 1 to the stamps list
def sol4():
    return [1, 1]

# Adding a stamp of value 2 to the stamps list
def sol5():
    return [1, 2, 2]

# Adding a stamp of value 3 to the stamps list
def sol6():
    return [1, 3]

# Adding a stamp of value 1 to the stamps list
def sol7():
    return [1, 1, 1]

# Adding a stamp of value 2 to the stamps list
def sol8():
    return [2]

# Adding a

if __name__ == "__main__":
    assert sat(sol())
