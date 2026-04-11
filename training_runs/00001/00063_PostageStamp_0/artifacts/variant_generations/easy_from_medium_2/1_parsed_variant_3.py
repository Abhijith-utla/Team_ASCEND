def sat(stamps: List[int], target=80, max_stamps=4, options=None):
    if options is None:
        options = [10, 32, 8]
    if len(stamps) > max_stamps:
        return False
    for s in stamps:
        if s not in options:
            return False
    return sum(stamps) == target

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
