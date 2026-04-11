def sat(li: List[int]):
    return all([(li[i] > li[i + 1]) for i in range(19)])

def sol():
    return {}

if __name__ == "__main__":
    assert sat(sol())
