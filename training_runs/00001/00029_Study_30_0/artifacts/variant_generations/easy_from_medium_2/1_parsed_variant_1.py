def sat(li: List[int]):
    return all([(li[i] % 1000 % 2 == 0) for i in range(20)])

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
