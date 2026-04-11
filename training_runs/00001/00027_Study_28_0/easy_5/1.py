def sat(li: List[int]):
    return all(i - j == 10 for i in li for j in li)

def sol():
    return [i for i in range(-10, 10) if i not in [i-10 for i in range(-10, 10)]]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
