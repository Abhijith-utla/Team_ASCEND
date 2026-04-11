def sat(stamps: List[int], target=271, max_stamps=8, options=[37, 37, 12, 87, 39]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# Correct answer:
def sol():
    return [37, 37, 12, 87, 39]

# Incorrect answers:
def sol():
    return [37, 37, 12, 87] # less than max_stamps

def sol():
    return [37, 37, 12, 87, 39, 39] # more than max_stamps

def sol():
    return [1, 2, 3, 4, 5] # sum is not target

def sol():
    return [37, 37, 12, 87, 39, 39, 1] # duplicate stamps

def sol():
    return [0, 1, 2, 3, 4] # sum is not target

def sol():
    return [1, 1, 1, 1, 1] # duplicate stamps

def sol():
    return [] # no stamps

if __name__ == "__main__":
    assert sat(sol())
