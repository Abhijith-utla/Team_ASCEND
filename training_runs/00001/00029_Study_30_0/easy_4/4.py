def sat(li: List[int]):
    return all([(li[i] % 1000 % 2 == 0) for i in range(20)])

def sol():
    return None

if __name__ == "__main__":
    assert sat(sol())
