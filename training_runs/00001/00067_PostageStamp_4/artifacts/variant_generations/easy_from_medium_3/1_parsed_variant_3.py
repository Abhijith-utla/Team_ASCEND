def sat(stamps: List[int], target=56, max_stamps=2, options=[25, 22, 8, 84, 60, 56]):
    return len(stamps) <= max_stamps and sum(stamps) == target

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
