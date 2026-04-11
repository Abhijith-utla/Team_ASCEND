def sat(stamps: List[int], target=80, max_stamps=4, options=[10, 32, 8]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
