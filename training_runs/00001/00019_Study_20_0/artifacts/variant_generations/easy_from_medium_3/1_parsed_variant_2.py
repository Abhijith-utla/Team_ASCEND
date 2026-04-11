def sat(li: List[int]) -> bool:
    return all([j == 3 * i for j, i in enumerate(li)])

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
