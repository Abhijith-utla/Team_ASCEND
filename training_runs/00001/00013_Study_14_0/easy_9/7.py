def sat(li: List[int]):
    return all([i <= j for i in li for j in li if i > j])

def sol():
    return True

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
