def sat(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    li = [4]
    for _ in range(989):  # Populate the list with 989 numbers from 1 to 1000
        li.append(li[-1] + 1)
    return li

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
