def sat(stamps: List[int], target=80, max_stamps=4, options=[20, 32, 8]):
    if len(stamps) > max_stamps:
        return False
    return sum(stamps) == target

def sol():
    return []

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
