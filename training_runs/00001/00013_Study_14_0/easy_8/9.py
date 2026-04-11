def sat(li: List[int]):
    return all([i == li[j] + li[j+1] for i in range(len(li))])

def sol():
    return [1, 2, 3, 4, 5]

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
