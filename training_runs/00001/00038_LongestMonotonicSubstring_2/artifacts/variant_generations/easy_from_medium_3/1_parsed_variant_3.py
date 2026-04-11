def sat(x):
    return all(ord(x[i]) <= ord(x[i + 1]) for i in range(len(x) - 1))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
