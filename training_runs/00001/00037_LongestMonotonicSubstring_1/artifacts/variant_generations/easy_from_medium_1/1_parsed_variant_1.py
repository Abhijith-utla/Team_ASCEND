def sat(x):
    return all(i <= j for i, j in enumerate(x))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
