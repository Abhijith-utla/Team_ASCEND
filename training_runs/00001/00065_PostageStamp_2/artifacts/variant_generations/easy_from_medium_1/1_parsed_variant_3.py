def sat(stamps: List[int]):
    if len(stamps) != 5:
        return False
    if sum(stamps) != 20:
        return False
    return True

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
