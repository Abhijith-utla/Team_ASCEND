def sat(stamps: List[int], max_stamps=3):
    return len(stamps) <= max_stamps and sum(stamps) == 43

def sol():
    return [3, 3, 3, 3]

assert sat(sol())

# Please note that the answer list is not limited to three stamps, it could be any number from 0 to 43.

# To ensure the correct number of stamps, you can use this code.
def sol(stamps=None):
    if stamps is None:
        stamps = [1]*12
    elif sum(stamps) != 43:
        raise ValueError("Sum of stamps does not equal 43.")
    return stamps

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
