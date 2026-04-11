def sat(li: List[int]):
    return all(abs(i - j) >= 10 for i in li for j in li)

def sol():
    return [i for i in range(-100, 101) if all(abs(i - j) >= 10 for j in range(-100, 101))]

if __name__ == "__main__":
    assert sat(sol())
