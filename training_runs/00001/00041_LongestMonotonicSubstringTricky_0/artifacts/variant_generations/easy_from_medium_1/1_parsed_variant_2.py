def sat(x):
    return all(x[i] <= x[i + 1] for i in range(len(x)))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
