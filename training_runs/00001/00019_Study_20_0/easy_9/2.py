def sat(li: List[int]) -> bool:
    return all(i == 3 * j for j, i in enumerate(li))

def sol():
    return [3, 6, 9]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
