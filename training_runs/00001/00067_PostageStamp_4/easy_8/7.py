def sat(stamps: List[int], target=60, max_stamps=1, options=[25, 22, 8, 84, 60, 56]):
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return [25, 22, 8, 84, 60, 56]

print(sol())

if __name__ == "__main__":
    assert sat(sol())
