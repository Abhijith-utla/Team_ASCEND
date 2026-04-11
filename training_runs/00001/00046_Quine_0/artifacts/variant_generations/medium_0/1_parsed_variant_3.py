def sat(quine):
    return eval(quine + "()")

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
