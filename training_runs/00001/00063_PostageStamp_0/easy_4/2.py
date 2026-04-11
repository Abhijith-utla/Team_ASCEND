def sat(stamps: List[int], target=80, max_stamps=4):
    if len(stamps) > max_stamps:
        return False
    return sum(stamps) == target

def sol():
    return []

# Checker function to test whether or not the solution function sol() returns the expected output
def checker():
    assert sat([])
    assert not sat([10, 20, 30, 40])
    assert sat([10, 10, 10, 10])
    assert not sat([10, 10, 10, 11])
    assert sat([10, 20, 30, 40, 50])

# Running the checker function
checker()

if __name__ == "__main__":
    assert sat(sol())
