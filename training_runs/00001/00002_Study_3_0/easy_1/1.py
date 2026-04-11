def sat(li: List[int]):
    return sorted(li) == list(range(len(li))) and all(li[i] != i for i in range(len(li))) and len(li) == 1000

def sol():
    return [i for i in range(1000) if i not in [x for x in range(1000)]]

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
