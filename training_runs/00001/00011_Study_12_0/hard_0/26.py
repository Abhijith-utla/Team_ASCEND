def sat(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    li = [4]
    for _ in range(989):  # fill the list with 4s and 999 others
        li.extend([4, 999])
    return li

print(sol())

if __name__ == "__main__":
    assert sat(sol())
