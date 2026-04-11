def sat(li: List[int]):
    return all(i + j == 3 for i, j in zip([6] + li, li)) and len(li) == 1000

def sol():
    return [6] + [0]*998

# Checker code
def sat(li: List[int]):
    return all(i + j == 3 for i, j in zip([6] + li, li)) and len(li) == 1000

if __name__ == "__main__":
    assert sat(sol())
