def sat(li: List[int]):
    return all(x == sum(li[:i]) for i in range(20))

def sol():
    return 1

# The function `sat` is already defined by the user, but here is the function `sol` defined to return 1.

if __name__ == "__main__":
    assert sat(sol())
