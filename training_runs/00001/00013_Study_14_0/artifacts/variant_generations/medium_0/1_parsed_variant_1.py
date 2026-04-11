def sat(li: List[int]):
    return all([i < sum(li[:i]) for i in range(20)])

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
