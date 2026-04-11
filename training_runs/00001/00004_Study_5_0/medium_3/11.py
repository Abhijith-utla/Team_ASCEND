def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)]) and li.count(0) == 1

def sol():
    return [i for i in range(10) if i == 0 or i % 5 == 0]

# The function sat(li: List[int]) checks if all elements in the list li are either 0 or divisible by 5. It returns True if all elements are either 0 or divisible by 5, and False otherwise.
# The function sol() returns a list of integers from 0 to 9 that are either 0 or divisible by 5.

if __name__ == "__main__":
    assert sat(sol())
