def sat(ls: List[str]):
    return "".join(ls) == '12345678' and all(len(s) == 8 for s in ls)

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
