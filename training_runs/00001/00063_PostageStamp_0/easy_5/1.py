def sat(stamps: List[int], target=80, max_stamps=4, options=[10, 32, 8]):
    if len(stamps) > max_stamps:
        return False
    for s in stamps:
        if s not in options:
            return False
    return sum(stamps) == target

def sol():
    return []

print(sat([10, 10, 10, 10], 210, 4, [10, 10, 10, 10]))  # True
print(sat([10, 10, 10, 10], 200, 4, [10, 10, 10, 10]))  # False
print(sat([10, 32, 8], 80, 4, [10, 32, 8]))  # True
print(sat([10, 32, 8], 80, 4, [32, 32, 32]))  # False
print(sat([10, 32, 8], 80, 4, [10, 10, 10]))  # False
print(sat([], 80, 4, [10, 32, 8]))  # True
print(sat([10, 32, 8, 1

if __name__ == "__main__":
    assert sat(sol())
