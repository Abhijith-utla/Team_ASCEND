def sat(li: List[int]):
    return all([(li[i] + li[i + 1] > 1000) for i in range(19)])

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
