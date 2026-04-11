def sat(stamps: List[int], target=80, max_stamps=4, options=[10, 32, 8]):
    if len(stamps) > max_stamps:
        return False
    return sum(stamps) == target

def sol():
    return [4, 1, 3, 1]

if __name__ == "__main__":
    assert sat(sol())
