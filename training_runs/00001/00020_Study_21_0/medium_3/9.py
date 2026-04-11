def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(7)]) and len(set(li)) == 3

def sol():
    return [1, 2, 2, 3, 3, 3, 4]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
