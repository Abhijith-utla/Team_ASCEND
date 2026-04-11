def sat(stamps: List[int], target=80, max_stamps=4, options=[10, 32, 8]):
    if len(stamps) > max_stamps:
        return False
    for s in stamps:
        if s not in options:
            return False
    return sum(stamps) == target

def sol():
    return []

print(sat([]))
print(sat([10]))
print(sat([10, 32]))
print(sat([10, 32, 8]))
print(sat([10, 32, 8, 20]))
print(sat([10, 32, 8, 20], 60, 3, [10, 32, 8, 20]))

if __name__ == "__main__":
    assert sat(sol())
