def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(5)])

def sol():
    return [4, 2, 3, 5, 1]

if __name__ == "__main__":
    assert sat(sol())
