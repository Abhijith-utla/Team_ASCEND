def sat(stamps: List[int], target=271, max_stamps=8, options=[37, 37, 12, 87, 39]):
    if len(stamps) > max_stamps:
        return False
    for s in stamps:
        if not isinstance(s, int):
            return False
        if s not in options:
            return False
    if sum(stamps) != target:
        return False
    return True

def sol():
    return []

print(sat([]))
print(sat([37]))
print(sat([37, 12]))
print(sat([37, 12, 39]))
print(sat([37, 12, 39], max_stamps=7))
print(sat([37, 12, 39], options=[37, 12, 39, 87]))
print(sat([37, 12, 39], options=[37, 12, 39, 87], max_stamps=7))
print(sat([37, 12, 39, 87, 39], target=377))
print(sat([37, 12, 39, 87, 39], target=271, options=[37, 12, 39, 87, 39]))
print(sat([37, 12, 39, 87, 39], target

if __name__ == "__main__":
    assert sat(sol())
