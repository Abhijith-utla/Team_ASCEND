def sat(rev_quine: str):
    return eval(rev_quine) == rev_quine.strip()

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
