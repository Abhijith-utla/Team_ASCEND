def sat(li: List[int]):
    return all([i <= j for i in li for j in li if i > j])

def sol():
    li = [1, 2, 3, 4, 5]
    return all([i <= j for i in li for j in li if i > j])

if __name__ == "__main__":
    assert sat(sol())
