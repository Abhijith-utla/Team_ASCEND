def sat(li: List[int]):
    return all(x + 1 == (2 ** x) - 1 for x in range(20))

def sol():
    return 10

def sat(li: List[int]):
    return all(x + 1 == (2 ** x) - 1 for x in range(20))

# Let's check if the function works
print(sat(sol()))  # Expected output: True

if __name__ == "__main__":
    assert sat(sol())
