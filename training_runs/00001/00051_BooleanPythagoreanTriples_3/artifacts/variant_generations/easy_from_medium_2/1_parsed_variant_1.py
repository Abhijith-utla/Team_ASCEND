def sat(lst: List[str]):
    return all(int(lst[i]) <= int(lst[i+1]) for i in range(len(lst)-1))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
