def sat(stamps: List[int], target=19):
    unique_stamps = set(stamps)
    for s in unique_stamps:
        if (s not in [19, 14, 81] and s != target):
            return False
    return len(unique_stamps) <= 1 and sum(stamps) == target

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
