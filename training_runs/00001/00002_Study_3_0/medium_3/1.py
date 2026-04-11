def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)-1))

def sol():
    return sorted(list(range(999)))

# Testing the function
def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)-1))

# Assertion statement
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
