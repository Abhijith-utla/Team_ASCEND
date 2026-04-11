def sat(li: List[int]):
    return all(x + 1 == (2 ** x) - 1 for x in range(20))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
