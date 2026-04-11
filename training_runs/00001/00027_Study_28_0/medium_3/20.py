def sat(li: List[int]):
    return all(abs(i - j) >= 10 for i in li for j in li if i != j) and len(li) == 100

def sol():
    return [i for i in range(100) if all(abs(i - j) >= 10 for j in range(100))]

# This is a test case you can use to check the correctness of your solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
