def sat(x):
    return all(x[i] <= x[i + 1] for i in range(len(x))) if len(x) > 0 else False

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
