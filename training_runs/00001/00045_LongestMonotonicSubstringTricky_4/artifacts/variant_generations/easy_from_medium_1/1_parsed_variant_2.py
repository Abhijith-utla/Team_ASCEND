def sat(x):
    return all(len(x[i]) <= len(x[i + 1]) and x[i + 1] > x[i] for i in range(len(x) - 1))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
