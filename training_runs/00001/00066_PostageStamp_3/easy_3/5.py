def sat(stamps: List[int], target=19, max_stamps=2, options=[19, 14, 81]):
    for s in stamps:
        if s not in options:
            return False
    return (len(stamps) <= max_stamps and sum(stamps) == target)  # No need to check the options

def sol():
    return [19]

if __name__ == "__main__":
    assert sat(sol())
