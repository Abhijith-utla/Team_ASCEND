def sat(quine):
    return eval(quine[::-1]) == quine

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
