def sat(li: List[int]):
    return all([li[i] != li[i + 2] for i in range(len(li) - 1)]) and len(set(li)) == 3

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
