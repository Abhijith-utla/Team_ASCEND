def sat(stamps: List[int]):
    return len(stamps) <= 3 and sum(stamps) == 18

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
