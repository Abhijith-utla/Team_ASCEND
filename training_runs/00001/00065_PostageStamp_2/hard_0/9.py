def sat(stamps: List[int], target=3, max_stamps=3, options=[18, 1, 43, 81]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return [18, 1, 43, 81]

# To ensure that the function `sol` returns a valid Python list, replace `return` with the actual answer. 
# The current answer is just an example, and may not work as expected.

if __name__ == "__main__":
    assert sat(sol())
