def sat(ls, idx1=-1, idx2=-1, value=None):
    if idx1 < 0 or idx2 < 0 or value is None:
        return False  # If any of the indices or value is invalid, it cannot be correct
    return ls[idx1] in ls[idx2] and ls[idx1] != value

def sol():
    def sat(ls, idx1=-1, idx2=-1, value=None):
        if idx1 < 0 or idx2 < 0 or value is None:
            return False  # If any of the indices or value is invalid, it cannot be correct
        return ls[idx1] in ls[idx2] and ls[idx1] != value

    # Assume we have a list called `ls` which we want to check
    # We also have two indices `idx1` and `idx2`
    # We also have a value `value`
    # We want to check if `ls[idx1]` is in `ls[idx2]` and `ls[idx1]` is not equal to `value`

    # Testing the function
    assert sat([1, 2, 3, 4, 5], 0, 2, 3)  # True
    assert sat([1, 2, 3, 4, 5], 0, 4, 5)  # False
    assert sat([1, 2, 3, 4

if __name__ == "__main__":
    assert sat(sol())
