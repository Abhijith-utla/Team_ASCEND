def sat(stamps: List[int]):
    if len(stamps) != 5:
        return False
    if sum(stamps) != 20:
        return False
    return True

def sol():
    return [1, 1, 1, 1, 1]

print(sol())

# Checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
