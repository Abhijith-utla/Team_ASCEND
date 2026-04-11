def sat(y):
    assert '__' not in y and '_' not in y and '9' not in y, "The string should not contain '__', '9' or '_'"
    return True

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
