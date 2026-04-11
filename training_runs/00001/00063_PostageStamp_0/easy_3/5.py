def sat(stamps: List[int], max_stamps=4, options=[10, 32, 8]):
    for s in stamps:
        if s not in options:
            return False
    return len(stamps) <= max_stamps

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())
