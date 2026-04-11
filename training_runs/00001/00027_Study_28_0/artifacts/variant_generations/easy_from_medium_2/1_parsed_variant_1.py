def sat(li: List[int]):
    return all(abs(i - j) >= 10 for i in li for j in li)

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
