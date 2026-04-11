def sat(ls: List[str]):
    return "".join(ls) == str(7 ** 64.5) and all(len(s) == 8 for s in ls)

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
