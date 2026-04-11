def sat(li: List[int]):
    return all(x == li[i] for i in range(len(li)))

def sol():
    return [1, 2, 3, 4, 5]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
