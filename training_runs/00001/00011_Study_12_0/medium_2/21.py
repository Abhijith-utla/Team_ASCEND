def sat(li: List[int]):
    return all(i + j == 2 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    li = [4]
    for i in range(989):
        li.append(li[-1] + li[-2])
    return li

if __name__ == "__main__":
    assert sat(sol())
