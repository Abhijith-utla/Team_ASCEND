def sat(li: List[int]):
    return all([(li[i] % 2 == 0 and li[i] % 123 == 0) for i in range(20)])

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
