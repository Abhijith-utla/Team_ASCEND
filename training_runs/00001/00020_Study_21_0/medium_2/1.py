def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(8)]) and len(set(li)) == 3

def sol():
    li = [2, 3, 5, 4, 7, 1, 3, 2]
    return li

if __name__ == "__main__":
    assert sat(sol())
