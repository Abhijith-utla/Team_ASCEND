def sat(stamps: List[int], target=19, max_stamps=2, options=[19, 14, 81]):
    unique_stamps = set(stamps)
    for s in unique_stamps:
        if s not in options:
            return False
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return [19, 14, 81]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
