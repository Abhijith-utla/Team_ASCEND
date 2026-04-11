def sat(stamps: List[int], target=80):
    for s in stamps:
        if s != 10 and s != 32 and s != 8:
            return False
    return sum(stamps) == target

def sol():
    stamps = [10, 32, 8]
    return stamps

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
