def sat(stamps: List[int], target=19):
    unique_stamps = set(stamps)
    for s in unique_stamps:
        if s not in [19, 14, 81]:
            return False
    return len(unique_stamps) <= 2 and sum(stamps) == target

def sol():
    return [1, 2, 3, 4, 5]

if __name__ == "__main__":
    assert sat(sol())
