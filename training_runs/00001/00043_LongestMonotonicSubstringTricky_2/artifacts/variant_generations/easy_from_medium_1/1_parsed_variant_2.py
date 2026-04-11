def sat(x: List[int], length=1):
    return all(x[i] < x[i + 1] for i in range(length))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
