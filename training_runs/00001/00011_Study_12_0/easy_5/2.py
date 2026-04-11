def sat(li: List[int]):
    return all(i + j == 4 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    # Create a list of size 1000 with sum of 4
    li = [4] + [0] * 999
    return li

if __name__ == "__main__":
    assert sat(sol())
