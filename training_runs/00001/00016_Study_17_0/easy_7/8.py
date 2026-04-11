def sat(i: int) -> bool:
    return len(str(i + 1000)) < len(str(i + 1001))

def sol():
    return sat(1000)

# The function `sat` checks if the difference in length of the two sequences of digits is less than 1000. 
# For example, if `i` is 1000, `len(str(i + 1000))` will be 4 (the number of digits in 1000 + 1000), 
# and if `i` is 1001, `len(str(i + 1001))` will be 5 (the number of digits in 1001 + 1000), 
# so the function will return `True` if `i` is less than 1001, and `False` otherwise.

if __name__ == "__main__":
    assert sat(sol())
