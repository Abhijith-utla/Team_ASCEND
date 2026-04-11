def sat(stamps: List[int]):
    if len(stamps) != 5:
        return False
    if sum(stamps) != 20:
        return False
    return True

def sol():
    stamps = [1, 1, 1, 1, 1]
    return stamps

print(sol())

# This code will return [1, 1, 1, 1, 1]

# To make sure the answer is correct, you can check the solution as follows:
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
