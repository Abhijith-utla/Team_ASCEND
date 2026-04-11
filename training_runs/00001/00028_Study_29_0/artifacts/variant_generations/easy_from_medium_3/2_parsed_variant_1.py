def sat(l: list):
    return all(i in range(996) for i in l if abs(i * i - j * j) >= 10 for j in l)

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
