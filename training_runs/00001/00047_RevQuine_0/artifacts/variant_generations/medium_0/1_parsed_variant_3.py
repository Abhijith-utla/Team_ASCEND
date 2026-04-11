def sat(rev_quine: str):
    return eval(rev_quine[::-1]) == rev_quine[0]

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
