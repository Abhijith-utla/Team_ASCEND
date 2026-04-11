def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(8)]) and len(set(li)) == 3

def sol():
    return [2, 1, 3, 2, 4, 3, 5, 6]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
