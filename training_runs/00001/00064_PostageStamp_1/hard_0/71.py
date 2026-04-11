def sat(stamps: List[int], target=271, max_stamps=8, options=[37, 37, 12, 87, 39]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

print(sat([], 271, 8, [37, 37, 12, 87, 39]))  # True
print(sat([37], 271, 8, [37, 37, 12, 87, 39]))  # False
print(sat([37, 37], 271, 8, [37, 37, 12, 87, 39]))  # False
print(sat([37, 37, 12], 271, 8, [37, 37, 12, 87, 39]))  # False
print(sat([37, 37, 12, 87], 271, 8, [37, 37, 12, 87, 39]))  # False
print(sat([37, 37, 12, 87, 39], 271, 8

if __name__ == "__main__":
    assert sat(sol())
