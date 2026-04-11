def sat(x: List[int]):
    return len(x) > 0

def sol():
    return []

# The function 'sat' checks if the input list 'x' is not empty, which means the list has at least one element. 
# If it's empty, the list does not satisfy the condition, so an empty list is returned.

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
