def sat(li: List[int]):
    return all(x >= 0 and x in range(20) for x in li)

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
