def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(7)]) and len(set(li)) == 3

def sol():
    from random import shuffle
    li = [i for i in range(3)]
    shuffle(li)
    while not sat(li):
        shuffle(li)
    return li

# Explanation:
# The function `sat` checks if the list `li` satisfies certain conditions.
# It first checks if all elements in the list are different, using list comprehension.
# It then checks if there are exactly three unique elements in the list, using the `set` function and the length of the list.
# The `shuffle` function is used to randomly rearrange the elements in the list.
# The loop continues until the list satisfies all conditions, ensuring a random solution.

if __name__ == "__main__":
    assert sat(sol())
