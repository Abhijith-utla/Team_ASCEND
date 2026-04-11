def sat(li: List[int]):
    return all(i not in li for i in range(1000)) and abs(min(li)-max(li)) < 10

def sol():
    li = [i for i in range(1000)]
    return sat(li)

# Test the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
