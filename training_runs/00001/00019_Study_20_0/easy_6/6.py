def sat(li: List[int]) -> bool:
    return all(li[i] != li[i + 1] for i in range(len(li) - 1)) and (li[0] < li[-1]) or (li[0] > li[-1])

def sol():
    li = [2, 1, 2, 1, 3]
    return sat(li)

print(sol())

if __name__ == "__main__":
    assert sat(sol())
