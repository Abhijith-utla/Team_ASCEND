def sat(li: List[int]):
    return all(i in range(1000) and abs(i - j) >= 10 for i in li for j in li if i != j) and len(set(li)) == 100

def sol():
    li = [i for i in range(1000) if abs(i - j) >= 10 for j in range(i+1, 1000) if i != j]
    li.append(999) # to ensure the last number is distinct
    return li

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
