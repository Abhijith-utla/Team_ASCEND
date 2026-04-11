def sat(target=19, stamps=[19, 14, 81], max_stamps=2, options=[19, 14, 81]):
    unique_stamps = set(stamps)
    for s in unique_stamps:
        if s not in options:
            return False
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return {
        'stamps': [19, 14, 81],
        'max_stamps': 2,
        'target': 19
    }

if __name__ == "__main__":
    assert sat(sol())
