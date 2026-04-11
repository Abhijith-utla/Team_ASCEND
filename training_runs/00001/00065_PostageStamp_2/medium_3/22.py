def sat(stamps: List[int], target=3, max_stamps=3, options=[18, 1, 43, 81]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# If the condition in the problem statement is not met, the answer should be an empty list.
# However, if the condition is met, the answer should contain a list of integers.
# This is a placeholder for the actual answer.

if __name__ == "__main__":
    assert sat(sol())
