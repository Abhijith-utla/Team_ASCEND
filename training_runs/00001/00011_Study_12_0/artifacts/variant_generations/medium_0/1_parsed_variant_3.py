def sat(li: List[int]):
    return all(i + j == 3 for i, j in zip([4] + li, li)) and len(li) == 1000

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
