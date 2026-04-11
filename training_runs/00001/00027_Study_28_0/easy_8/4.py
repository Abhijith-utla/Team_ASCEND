def sat(li):
    return not any(abs(i - j) < 10 for i in li for j in li if i != j) and len(li) == 100

def sol():
    li = [i for i in range(100)]
    return li

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
