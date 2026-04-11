def sat(li: List[int]) -> bool:
    return all(li[i] != li[i + 1] for i in range(len(li) - 1)) and (li[0] < li[-1]) or (li[0] > li[-1])

def sol():
    return [1, 2, 3, 2, 1]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
