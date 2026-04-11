def sat(stamps: List[int]):
    if len(stamps) != 5:
        return False
    if sum(stamps) != 20:
        return False
    return True

def sol():
    return [1, 2, 3, 4, 5]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
