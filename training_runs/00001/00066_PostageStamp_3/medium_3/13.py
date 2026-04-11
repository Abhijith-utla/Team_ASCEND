def sat(stamps: List[int], target=19, max_stamps=2, options=[19, 14, 81]):
    unique_stamps = set(stamps)
    for s in unique_stamps:
        if s not in options:
            return False
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# Testing
def test_sat():
    assert sat([19]) == False
    assert sat([19, 19]) == False
    assert sat([19, 14]) == False
    assert sat([19, 14, 14]) == False
    assert sat([19, 14, 14, 81]) == False
    assert sat([14, 14, 14, 81]) == True
    assert sat([14, 14, 14, 81, 81]) == False
    assert sat([14, 14, 14, 81, 81, 81]) == False
    assert sat([14, 14, 14, 81, 81, 81, 81]) == True
    print("All tests passed")

test_sat()

if __name__ == "__main__":
    assert sat(sol())
