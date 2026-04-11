def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(9)]) and len(set(li)) == 3

def sol():
    return [2, 2, 2, 2, 2, 2, 2, 2, 2]

if __name__ == "__main__":
    assert sat(sol())
