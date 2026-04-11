def sat(li: List[int]):
    return all(x == li[i] for i in range(len(li)))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
