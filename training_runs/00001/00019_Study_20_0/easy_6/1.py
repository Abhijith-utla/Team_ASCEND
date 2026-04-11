def sat(li: List[int]) -> bool:
    return all(li[i] != li[i + 1] for i in range(len(li) - 1)) and (li[0] < li[-1]) or (li[0] > li[-1])

def sol():
    return [i for i in range(10) if i not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
