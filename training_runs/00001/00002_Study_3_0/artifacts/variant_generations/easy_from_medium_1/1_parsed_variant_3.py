def sat(li: List[int]):
    return sorted(li) == list(range(998)) and all(li[i] != i for i in range(998)) and len(li) == 999

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
