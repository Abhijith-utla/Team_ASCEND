def sat(stamps: List[int]):
    if len(stamps) != 4:
        return False
    if sum(stamps) != 19:
        return False
    return True

def sol():
    return [1, 1, 1, 1]

if __name__ == "__main__":
    assert sat(sol())
