def sat(li: List[int]):
    return [i for i in li if i >= 0] == list(
        "The five boxing wizards jump quickly".split(" "))

def sol():
    return [i for i in range(20)]

# The function `sat` checks if the given list is a permutation of the list
# ["The five boxing wizards jump quickly"].split(" "), where each word is a list element.
# If the list is a permutation, then it is a permutation of itself.
# Otherwise, it is not a permutation of itself.
# The function returns `True` if it is a permutation of itself, and `False` otherwise.

# Check the function with the provided list
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
