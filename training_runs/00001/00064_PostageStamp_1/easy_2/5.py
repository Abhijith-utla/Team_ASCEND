def sat(stamps: List[int], target=271, max_stamps=8, options=[37, 37, 12, 87, 39]):
    if len(stamps) > max_stamps:
        return False
    for s in stamps:
        if not isinstance(s, int):
            return False
        if s not in options:
            return False
    if sum(stamps) != target:
        return False
    return True

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())
