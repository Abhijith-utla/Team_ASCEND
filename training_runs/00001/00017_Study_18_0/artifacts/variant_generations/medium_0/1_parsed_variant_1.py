def sat(ls: List[str]) -> bool:
    return all(s not in ls for s in ls)

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
