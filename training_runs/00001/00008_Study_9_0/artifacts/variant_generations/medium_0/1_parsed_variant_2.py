def sat(li: List[int]):
    return [i for i in li if i >= 0] == list(
        "The five boxing wizards jump quickly".split(" "))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
