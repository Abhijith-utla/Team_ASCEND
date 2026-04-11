def sat(stamps: List[int], target=80, max_stamps=4, options=[40, 32, 8]):
    if len(stamps) > max_stamps:
        return False
    return sum(stamps) == target

def sol():
    return [1, 1, 1, 1]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
