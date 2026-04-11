def sat(li: List[int]):
    return all(j in {i} for i, j in enumerate(li))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
