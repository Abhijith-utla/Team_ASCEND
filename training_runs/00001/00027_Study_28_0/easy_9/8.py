def sat(li):
    return all(abs(i - j) >= 10 for i in li for j in li if i != j) and len(li) == 100

def sol():
    return [x for x in range(-100, 100) if abs(x - 0) >= 10]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
