def sat(li: List[int]):
    return [chr(i) for i in li] == list("The quick brown fox jumps over the lazy dog".replace(" ", ""))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
