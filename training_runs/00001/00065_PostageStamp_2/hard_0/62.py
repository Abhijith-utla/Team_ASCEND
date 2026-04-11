def sat(stamps: List[int], target=3, max_stamps=3, options=[18, 1, 43, 81]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# The given function 'sat' does not solve the problem as it returns an empty list when all conditions are true.
# We need to return something in order to satisfy the problem conditions.
# For example, we can return the number 1:

def sol():
    return 1

if __name__ == "__main__":
    assert sat(sol())
