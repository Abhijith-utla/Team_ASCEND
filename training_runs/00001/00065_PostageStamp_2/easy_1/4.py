def sat(stamps: List[int]):
    if len(stamps) != 3:
        return False
    if sum(stamps) != 18:
        return False
    return True

def sol():
    return [3, 6, 6]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
