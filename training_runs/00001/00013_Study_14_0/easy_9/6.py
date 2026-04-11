def sat(li: List[int]):
    return all([i <= j for i in li for j in li if i > j])

def sol():
    def sat(li: List[int]):
        return all([i <= j for i in li for j in li if i > j])

    return sat([1, 2, 3])

print(sol())

if __name__ == "__main__":
    assert sat(sol())
