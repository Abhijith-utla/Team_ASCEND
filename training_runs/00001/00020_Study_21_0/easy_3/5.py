def sat(li: List[int]):
    return all([li[i] != li[i + 2] for i in range(len(li) - 1)]) and len(set(li)) == 3

def sol():
    return []

# This function should return an answer object that contains a single integer value.
# In Python, an answer object can be created using the 'return' statement.
# The function should return a list of integers.
# You might use a list comprehension to generate a list of integers.
# Remember that a list in Python is an ordered sequence of elements, and you can access an element by its index.
# Here is an example of how you might use it:

def sol():
    return [1, 2, 3]

print(sol())

if __name__ == "__main__":
    assert sat(sol())
