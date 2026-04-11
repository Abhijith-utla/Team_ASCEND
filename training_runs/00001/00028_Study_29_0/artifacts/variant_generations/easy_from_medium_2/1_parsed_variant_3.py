def sat(l: list):
    return all(i in range(1000) for i in l if i not in range(1000))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
