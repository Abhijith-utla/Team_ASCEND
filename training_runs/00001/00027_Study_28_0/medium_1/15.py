def sat(li: List[int]):
    return all(i not in li for i in range(1000)) and abs(min(li)-max(li)) < 10

def sol():
    return [i for i in range(1000) if i not in [j for j in range(1000)]]

print(sol())

# assert sat([i for i in range(1000) if i not in [j for j in range(1000)]])

if __name__ == "__main__":
    assert sat(sol())
