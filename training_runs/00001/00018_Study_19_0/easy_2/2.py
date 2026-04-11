def sat(li: List[int]):
    return sum(li) == 105

def sol():
    return [5, 10, 15, 20]

print(sat(sol()))  # True

if __name__ == "__main__":
    assert sat(sol())
