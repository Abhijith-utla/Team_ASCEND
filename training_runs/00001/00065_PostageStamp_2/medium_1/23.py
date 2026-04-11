def sat(stamps: List[int]):
    return len(stamps) <= 3 and sum(stamps) == 18

def sol():
    return [2, 5]

# This will assert that the given solution is correct
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
