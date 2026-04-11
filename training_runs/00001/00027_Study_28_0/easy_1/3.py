def sat(li: List[int]):
    return all(i not in li for i in range(1000)) and abs(min(li)-max(li)) < 10

def sol():
    li = [i for i in range(1000)]
    li.remove(max(li))
    li.remove(min(li))
    return li

print(sat(sol()))  # Expected output: [0, 1, 2, 3, 4, ..., 995, 996]

if __name__ == "__main__":
    assert sat(sol())
