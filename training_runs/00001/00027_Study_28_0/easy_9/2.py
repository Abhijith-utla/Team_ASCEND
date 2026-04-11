def sat(li):
    return all(abs(i - j) >= 10 for i in li for j in li if i != j) and len(li) == 100

def sol():
    return [i for i in range(-50, 50) if sat([i])]

if __name__ == "__main__":
    assert sat(sol())
