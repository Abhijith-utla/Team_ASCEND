def sat(li: List[int]) -> bool:
    return all(i == 3 * j for j, i in enumerate(li))

def sol():
    li = [1, 2, 3, 4, 5]
    return sat(li)

if __name__ == "__main__":
    assert sat(sol())
