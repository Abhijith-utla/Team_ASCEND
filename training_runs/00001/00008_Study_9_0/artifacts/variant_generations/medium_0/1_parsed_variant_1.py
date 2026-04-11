def sat(li: List[int]):
    return [ord(i) for i in li] == list(
        "The five boxing wizards jump quickly".replace(" ", ""))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
