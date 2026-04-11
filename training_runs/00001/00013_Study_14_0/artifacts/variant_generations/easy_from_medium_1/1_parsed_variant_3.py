def sat(li: List[int]):
    return all(li[i] < sum(li[:i-1]) if i > 0 else li[i] < sum(li) for i in range(len(li)))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
