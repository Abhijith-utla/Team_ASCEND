def sat(li: List[int]):
    return all([sum(li[:i]) == i for i in range(20)])

def sol():
    return [sum(i) for i in range(20)]

# Test case
print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
