def sat(stamps: List[int]):
    if len(stamps) != 4:
        return False
    if sum(stamps) != 19:
        return False
    return True

def sol():
    return [2, 5, 5, 10]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
