def sat(li: List[int]):
    return all(abs(i - j) >= 10 for i in li for j in li) and len(set(li)) == 10

def sol():
    return []

# This function is incorrect because the list has only one element and the condition of the all function is False
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
