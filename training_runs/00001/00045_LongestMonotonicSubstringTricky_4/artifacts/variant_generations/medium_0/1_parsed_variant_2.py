def sat(x: List[int], length=19):
    return all(x[i] <= x[i + 1] and x[i + 1] > x[i] for i in range(length - 1))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
