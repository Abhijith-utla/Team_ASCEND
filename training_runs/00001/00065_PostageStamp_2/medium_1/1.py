def sat(stamps: List[int]):
    return len(stamps) <= 3 and sum(stamps) == 18

def sol():
    return [2, 6, 6]

if __name__ == "__main__":
    assert sat(sol())
