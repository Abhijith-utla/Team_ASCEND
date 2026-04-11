def sat(stamps: List[int]):
    if len(stamps) != 3:
        return False
    if sum(stamps) != 18:
        return False
    return True

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
