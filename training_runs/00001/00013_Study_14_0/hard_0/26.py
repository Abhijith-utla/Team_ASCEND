def sat(li: List[int]):
    return all([sum(li[:i]) == i for i in range(20)])

def sol():
    return [i for i in range(20) if i == sum([sum(li[:i]) for li in range(20)])]

if __name__ == "__main__":
    assert sat(sol())
