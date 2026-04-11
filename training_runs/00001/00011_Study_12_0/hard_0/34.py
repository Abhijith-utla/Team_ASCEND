def sat(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    li = [4] + [i for i in range(1, 998) for _ in range(2)]  # Create a list with 1000 elements
    return li

if __name__ == "__main__":
    assert sat(sol())
