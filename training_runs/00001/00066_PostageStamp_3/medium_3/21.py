def sat(stamps: List[int], target=19, max_stamps=2, options=[19, 14, 81]):
    unique_stamps = set(stamps)
    for s in unique_stamps:
        if s not in options:
            return False
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return [19, 19, 19]

print(sat([19, 19, 19]))  # False
print(sat([19, 14, 81]))  # False
print(sat([19]))  # True
print(sat([19, 14, 80]))  # False

# This should pass if the function is correctly implemented
assert sat([19, 19, 19]) == False
assert sat([19, 14, 81]) == False
assert sat([19]) == True
assert sat([19, 14, 80]) == False

if __name__ == "__main__":
    assert sat(sol())
