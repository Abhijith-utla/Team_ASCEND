def sat(stamps: List[int], max_stamps=3):
    return len(stamps) <= max_stamps and sum(stamps) == 43

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
