def sat(li: List[int]):
    return all(x == sum(li[:i]) for i in range(1, len(li) + 1))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
