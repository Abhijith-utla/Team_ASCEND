def sat(li: List[int]):
    return all(x == i for i, x in enumerate(li))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
