def sat(answer):
    return all(a == b for a, b in zip(answer, 'de'))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
