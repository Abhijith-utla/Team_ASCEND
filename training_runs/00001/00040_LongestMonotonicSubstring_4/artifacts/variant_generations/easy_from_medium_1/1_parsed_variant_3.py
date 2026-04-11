def sat(x):
    return all(x[i] <= x[i + 1] for i in range(len(x) - 1)) if len(x) > 1 else True

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
