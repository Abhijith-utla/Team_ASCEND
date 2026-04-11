def sat(stamps: List[int], max_stamps=3):
    return len(stamps) <= max_stamps and sum(stamps) == 43

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())
