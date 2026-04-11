def sat(li: List[int]):
    return all(sum(li[:i]) == 2 ** i - 1 for i in range(20))

def sol():
    li = [0] * 20
    return li

if __name__ == "__main__":
    assert sat(sol())
