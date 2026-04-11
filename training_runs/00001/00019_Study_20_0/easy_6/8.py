def sat(li: List[int]) -> bool:
    return all(li[i] != li[i + 1] for i in range(len(li) - 1)) and (li[0] < li[-1]) or (li[0] > li[-1])

def sol():
    li = [2, 3, 4, 1, 5]
    return sat(li)

# Testing the function
print(sol())  # should return True

# The function should return True if the list is a strictly increasing sequence, decreasing sequence or a decreasing sequence starting with a greater than ending with a less than. Otherwise, it should return False.

if __name__ == "__main__":
    assert sat(sol())
