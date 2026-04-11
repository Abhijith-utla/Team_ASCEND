def sat(li: List[int]):
    return all(j in {i - 1, i + 1, 3 * i} for i, j in zip([0] + li, li + [128]))

def sol():
    return [0]

# The function sat checks if all the elements of the list are in the set {i - 1, i + 1, 3 * i} for any index i in the list. 
# The set is created by taking all elements from 0 to 127 in steps of 1 and 3, then adding 128 to the end, because we're looking for elements in the set {i - 1, i + 1, 3 * i} for any i in the list. 
# The function zip([0] + li, li + [128]) generates a list of tuples where the first element is the index and the second element is the corresponding element in the list. 
# The function all checks if all elements in the list are True, and returns True if all elements are True, and False otherwise.

assert sat([0])

if __name__ == "__main__":
    assert sat(sol())
