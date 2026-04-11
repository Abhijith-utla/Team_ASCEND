def sat(li: List[int]):
    return all(x >= 0 and 2 ** x - 1 == (2 ** x) - 1 for x in li)

def sol():
    return 1

# The function 'sat' is already defined by the user.
# The function 'sol' is defined to return 1.

if __name__ == "__main__":
    assert sat(sol())
