def sat(stamps: List[int], target=80):
    for s in stamps:
        if s != 10 and s != 32 and s != 8:
            return False
    return sum(stamps) == target

def sol():
    return [8, 32]

# Incorrect pattern:
# def sol():
#     return [8, 32, 8]

# Correct pattern:
# def sol():
#     return [10, 32]

if __name__ == "__main__":
    assert sat(sol())
