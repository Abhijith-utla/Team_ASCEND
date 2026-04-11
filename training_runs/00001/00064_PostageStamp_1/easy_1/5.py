def sat(stamps: List[int], target=271, max_stamps=8, options=[37, 37, 12, 87, 39]):
    if len(stamps) > max_stamps:
        return False
    for s in stamps:
        if not isinstance(s, int):
            return False
        if s not in options:
            return False
    return sum(stamps) == target

def sol():
    return [37, 37, 12, 87, 39]

# This assertion is for the correctness of the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
