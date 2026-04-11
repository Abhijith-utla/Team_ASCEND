def sat(li: List[int]):
    return all(j in {i - 1, i + 1, 3 * i} for i, j in zip([0] + li, li + [128]))

def sol():
    return 128

# Function to check if the list is sorted
def is_sorted(li: List[int]):
    return all(j <= i for i, j in zip(li, li[1:]))

# Function to check if the list is sorted and all elements are unique
def is_unique(li: List[int]):
    return is_sorted(li) and len(li) == len(set(li))

# Function to check if the list satisfies the condition
def sat(li: List[int]):
    return is_unique(li)

# Function to test the solution
def test():
    assert not sat([])
    assert not sat([1])
    assert sat([2])
    assert not sat([2, 2])
    assert not sat([2, 3])
    assert sat([1, 3, 6])
    assert not sat([3, 6, 9])
    assert sat([1, 2, 3, 4, 5, 6, 7, 8, 9,

if __name__ == "__main__":
    assert sat(sol())
