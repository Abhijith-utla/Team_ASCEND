def sat(stamps: List[int], target=19, max_stamps=2, options=[19, 14, 81]):
    for s in stamps:
        if s not in options:
            return False
    return (len(stamps) <= max_stamps and sum(stamps) == target)

def sol():
    return []

# The function 'sat' is already defined by the user.
# The function 'sol' is to construct and return a single answer value.
# The final checker will run: assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
