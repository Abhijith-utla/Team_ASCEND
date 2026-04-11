def sat(li: List[int]):
    return [chr(i) for i in li] == list("Hello World".replace(" ", ""))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
