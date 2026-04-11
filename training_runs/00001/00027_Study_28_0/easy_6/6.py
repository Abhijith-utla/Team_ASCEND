def sat(li: List[int]):
    return all(abs(i - j) >= 10 for i in li for j in li if i != j)

def sol():
    def sat(li: List[int]):
        return all(abs(i - j) >= 10 for i in li for j in li if i != j)
    return sat

if __name__ == "__main__":
    assert sat(sol())
