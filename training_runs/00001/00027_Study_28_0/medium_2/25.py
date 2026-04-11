def sat(li: List[int]):
    return all(abs(i - j) >= 10 for i in li for j in li) and len(set(li)) == 10

def sol():
    li = [i for i in range(-100, 100) if i != 0]
    return li

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
