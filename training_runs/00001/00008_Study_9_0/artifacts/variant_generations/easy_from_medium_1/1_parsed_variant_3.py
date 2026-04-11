def sat(li: List[str]):
    return sum([1 for i in li if ord(i) % 3 == 2]) == 0

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
