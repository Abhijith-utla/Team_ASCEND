def sat(stamps: List[int], target=3, max_stamps=3, options=[18, 1, 43, 81]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# This function tests the problem statement with a variety of inputs
def test():
    assert sat([18, 1, 43, 81]) == True
    assert sat([18, 1, 43, 79]) == False
    assert sat([18, 1, 43]) == True
    assert sat([18, 1, 43, 81], 10) == False
    assert sat([18, 1, 43, 81], 80, 4) == True
    assert sat([18, 1, 43, 81], 80, 2) == False

test()

if __name__ == "__main__":
    assert sat(sol())
