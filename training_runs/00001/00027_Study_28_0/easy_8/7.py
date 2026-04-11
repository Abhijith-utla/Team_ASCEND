def sat(li):
    return not any(abs(i - j) < 10 for i in li for j in li if i != j) and len(li) == 100

def sol():
    return [i for i in range(100) if all(abs(i - j) > 10 for j in range(100) if i != j)]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
