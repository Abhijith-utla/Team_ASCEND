def sat(stamps: List[int], target=19):
    unique_stamps = set(stamps)
    for s in unique_stamps:
        if s not in [19, 14, 81]:
            return False
    return len(unique_stamps) <= 2 and sum(stamps) == target

def sol():
    return {
        'stamps': [14, 14, 81],
        'target': 19,
        'unique_stamps': set([14, 14, 81]),
        'is_valid': len([14, 14, 81]) <= 2 and sum([14, 14, 81]) == 19
    }

print(sol())

if __name__ == "__main__":
    assert sat(sol())
