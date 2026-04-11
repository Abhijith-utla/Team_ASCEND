def sat(li: List[int]) -> bool:
    return all(i == 3 * j for j, i in enumerate(li))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
