def sat(stamps: List[int]):
    return len(stamps) <= 3 and sum(stamps) == 18

def sol():
    return [3, 3, 3, 1]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
