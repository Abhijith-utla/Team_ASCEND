def sat(li: List[int]):
    return all([sum(li[:i]) == i for i in range(20)])

def sol():
    return [i for i in range(20) if sum([i for j in range(i)]) != i]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
