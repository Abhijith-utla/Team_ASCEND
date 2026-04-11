def sat(li: List[int]) -> bool:
    return all(li[i] != li[i + 1] for i in range(len(li) - 1)) and (li[0] < li[-1]) or (li[0] > li[-1])

def sol():
    li = [3, 2, 3, 2, 4]
    return sat(li)

if __name__ == "__main__":
    assert sat(sol())
