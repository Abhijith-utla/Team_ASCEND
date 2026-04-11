def sat(li: List[int]):
    return set(li) == {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34}

def sol():
    return {}

# The correct answer is the list [0, 1, ..., 34]
# We just need to check if this list contains all numbers from 0 to 34.
# This can be achieved using a set and the set() function
def sat(li: List[int]):
    return set(li) == {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34}

if __name__ == "__main__":
    assert sat(sol())
