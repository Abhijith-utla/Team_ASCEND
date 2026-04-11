def sat(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol(li: List[int]):
    if len(li) == 0 or li[0] != 4:
        return False
    return sum(li) == 4005 and len(li) == 1000

print(sol([4]*1000))

if __name__ == "__main__":
    assert sat(sol())
