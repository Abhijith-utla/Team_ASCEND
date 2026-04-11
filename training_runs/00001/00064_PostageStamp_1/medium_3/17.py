def sat(stamps: List[int], target=271, max_stamps=8, options=[3, 3, 3, 3, 3]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# For the sake of testing, we can use Python's built-in function all()
# This function returns True if all elements of the iterable (list, tuple, etc.) are true.
# If not, it returns False.

assert all(sat(stamps) for stamps in [
    [],
    [3],
    [3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]])

if __name__ == "__main__":
    assert sat(sol())
