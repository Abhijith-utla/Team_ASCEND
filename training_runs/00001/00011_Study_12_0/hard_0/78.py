def sat(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    def sat(li: List[int]):
        return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

    li = [4] + [0] * 999  # Create a list with 1000 elements, all initialized to 0 except the first

if __name__ == "__main__":
    assert sat(sol())
