def sat(ls: List[str]):
    return all(len(s) == 8 for s in ls)

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
