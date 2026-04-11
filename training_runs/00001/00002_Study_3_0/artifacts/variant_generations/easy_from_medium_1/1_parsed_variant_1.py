def sat(li: List[int]):
    return sorted(li) == list(range(len(li))) and all(li[i] != i for i in range(len(li))) and len(li) == 1000

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
