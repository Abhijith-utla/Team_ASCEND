def sat(x):
    for i in range(len(x) - 1):
        if x[i] >= x[i + 1]:
            return False
    return True

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
