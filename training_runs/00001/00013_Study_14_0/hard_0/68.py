def sat(li: List[int]):
    return all([sum(li[:i]) == i for i in range(20)])

def sol():
    return all([sum(li[:i]) == i for i in range(20)])

print(sol())

if __name__ == "__main__":
    assert sat(sol())
