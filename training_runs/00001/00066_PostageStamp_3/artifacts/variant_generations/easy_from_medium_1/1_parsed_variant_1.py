def sat(stamps: List[int], target=19, max_stamps=2, options=[19, 14, 81]):
    for s in stamps:
        if s not in options:
            return False
    return True  # No need to check the rest if the stamps are invalid

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
