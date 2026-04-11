def sat(li: List[int]):
    return all(abs(i - j) >= 10 for i in li for j in li if i != j)

def sol():
    return [i for i in range(-100, 100) if sat([i])]

# This line is to make sure the solution is correct
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
