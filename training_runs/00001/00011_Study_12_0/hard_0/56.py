def sat(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol() -> int:
    li = [4]
    for _ in range(987):
        li.append(sum(li[-2:]))
    return sum(li)

print(sol())

if __name__ == "__main__":
    assert sat(sol())
