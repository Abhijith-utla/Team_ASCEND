def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(7)]) and len(set(li)) == 3

def sol():
    li = [3, 3, 3, 2, 2, 1, 1]
    return li

if __name__ == "__main__":
    assert sat(sol())
