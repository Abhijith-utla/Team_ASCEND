def sat(li):
    for i in li:
        for j in li:
            if abs(i - j) < 10:
                return False
    return len(li) == 100

def sol():
    return [i for i in range(100) if i not in range(0, 10)]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
