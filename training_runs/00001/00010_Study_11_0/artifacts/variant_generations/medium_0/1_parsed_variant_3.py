def sat(ls: List[str]):
    if len(ls) == 0:
        return True
    else:
        return all(len(set(i)) == len(ls[0]) for i in ls)

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
