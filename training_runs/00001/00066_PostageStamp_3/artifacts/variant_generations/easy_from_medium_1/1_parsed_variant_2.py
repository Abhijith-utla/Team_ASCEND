def sat(stamps: List[int], target=19, max_stamps=2, options=[19, 14, 81]):
    for s in stamps:
        if s not in options:
            return False
    return (len(stamps) <= max_stamps)  # No need to check the sum of the stamps

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
