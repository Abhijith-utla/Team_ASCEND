def sat(stamps: List[int], target=80, max_stamps=4, options=[10, 32, 8]):
    if len(stamps) > max_stamps:
        return False
    for s in stamps:
        if s not in options:
            return False
    return sum(stamps) == target

def sol():
    return [10, 20, 30, 40]

print(sat(sol()))  # False
print(sat([10, 20, 30]))  # True

if __name__ == "__main__":
    assert sat(sol())
