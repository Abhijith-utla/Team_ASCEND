def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(8)]) and len(set(li)) == 3

def sol():
    li = [1, 2, 2, 3, 3, 3, 4, 4]
    return li

if __name__ == "__main__":
    assert sat(sol())
