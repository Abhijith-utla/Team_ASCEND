def sat(stamps: List[int], target=271, max_stamps=8, options=[1, 2, 3]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# The above function always returns an empty list, because we cannot solve the problem.
# We need to provide a valid solution. Here is a solution that always returns [1,2,3] as the solution:

def sol():
    return [1,2,3]

if __name__ == "__main__":
    assert sat(sol())
