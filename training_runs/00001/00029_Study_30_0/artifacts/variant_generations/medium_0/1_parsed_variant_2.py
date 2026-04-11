def sat(li: List[int]):
    return all([((123 * li[i] % 1000 < 123 * li[i + 1] % 1000) and (li[i] in range(1000))) for i in range(20)])

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
