def sat(li: List[int]):
    return all(j == 3 * i for i, j in enumerate(li))

def sol():
    return [3]*100000

# The problem is that the answer list is a list of 100,000 integers each equal to 3. The function 'sat' checks if all elements of the list are multiples of 3.

# So, the function 'sol' returns a list of 100,000 integers each equal to 3.

if __name__ == "__main__":
    assert sat(sol())
