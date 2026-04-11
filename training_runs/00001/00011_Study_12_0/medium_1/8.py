def sat(li: List[int]):
    return all(i + j == 1 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    return 5

# Uncomment the following line to test your solution
# assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
