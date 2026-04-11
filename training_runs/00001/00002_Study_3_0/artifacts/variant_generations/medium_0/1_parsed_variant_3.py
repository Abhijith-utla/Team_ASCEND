def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)-1))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
