def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(5)])

def sol():
    return [i for i in range(5) if i % 2 == 0]

# testing the solution
print(sol())

def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(5)])

# testing the solution
print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
