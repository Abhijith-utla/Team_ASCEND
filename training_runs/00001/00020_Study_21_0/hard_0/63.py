def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3

def sol():
    li = [2, 3, 1, 2, 3, 4, 5, 5, 6, 7]
    return li

if __name__ == "__main__":
    assert sat(sol())
