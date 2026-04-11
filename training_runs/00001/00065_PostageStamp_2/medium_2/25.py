def sat(stamps: List[int], max_stamps=3):
    return len(stamps) <= max_stamps and sum(stamps) == 43

def sol():
    return []

# To validate the solution, we run the function and assert it returns an empty list.
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
