def sat(li: List[int]):
    return all(li[i] < sum(li[:i+1]) for i in range(len(li)))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
