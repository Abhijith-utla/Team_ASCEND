def sat(rev_quine: str):
    return eval(rev_quine) == rev_quine

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
