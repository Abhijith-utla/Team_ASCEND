def sat(ls: List[str]) -> bool:
    return all(len(set(s)) == len(s) for s in ls)

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
