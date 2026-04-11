def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(9)]) and len(set(li)) == 3

def sol():
    return [1, 2, 2, 4, 4, 4, 7, 7, 9]

if __name__ == "__main__":
    assert sat(sol())
