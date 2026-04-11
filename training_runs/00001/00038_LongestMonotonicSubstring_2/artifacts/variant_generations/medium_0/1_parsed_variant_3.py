def sat(x: List[str], length=737):
    return all(x[i] <= x[i + 1] for i in range(length - 1))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
