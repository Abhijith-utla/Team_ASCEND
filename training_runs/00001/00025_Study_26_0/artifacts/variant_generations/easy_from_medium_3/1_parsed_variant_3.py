def sat(ls: List[str]):
    return "".join(ls) == '123456789' and all(len(s) == 9 for s in ls)

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
