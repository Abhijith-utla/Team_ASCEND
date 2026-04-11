def sat(stamps: List[int]):
    if len(stamps) != 4:
        return False
    if sum(stamps) != 19:
        return False
    return True

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
