def sat(li: List[int]):
    return all(li[i] < sum(li[:i]) for i in range(1, len(li)))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
