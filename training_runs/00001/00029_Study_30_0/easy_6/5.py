def sat(li: List[int]):
    return all([(li[i] + li[i + 1] > 1000) for i in range(19)])

def sol():
    return []

# The function `sat` is already defined by the user, we are not redefining it.

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
