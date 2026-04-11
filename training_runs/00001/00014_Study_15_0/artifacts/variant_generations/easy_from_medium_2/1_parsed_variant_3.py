def sat(li: List[int]):
    return all(x + y == 2 ** x for x in range(20) for y in li[:x + 1])

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
