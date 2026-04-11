def sat(li: List[int]):
    return all([i <= j for i in li for j in li if i > j])

def sol():
    return sat

def sat(li: List[int]):
    return all([i <= j for i in li for j in li if i > j])

if __name__ == "__main__":
    assert sat(sol())
