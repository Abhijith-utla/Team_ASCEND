def sat(stamps: List[int]):
    return len(stamps) <= 3 and sum(stamps) == 18

def sol():
    return [1, 1, 1, 1]

if __name__ == "__main__":
    assert sat(sol())
