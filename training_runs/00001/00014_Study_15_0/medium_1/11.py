def sat(li: List[int]):
    return all(x + 1 == (2 ** x) - 1 for x in range(20))

def sol():
    return [x + 1 for x in range(20) if (2 ** x) - 1 == (2 ** (x + 1)) - 1]

# The function sat(li: List[int]) is already defined by the user.
# Therefore, we don't need to implement it.

# We can verify that sol() returns the correct answer with the following code:

def test_sol():
    assert sat(sol())

test_sol()

if __name__ == "__main__":
    assert sat(sol())
