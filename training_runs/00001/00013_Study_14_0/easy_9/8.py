def sat(li: List[int]):
    return all([i <= j for i in li for j in li if i > j])

def sol():
    return [i for i in range(10) if all([i <= j for j in range(i)])]

if __name__ == "__main__":
    assert sat(sol())
