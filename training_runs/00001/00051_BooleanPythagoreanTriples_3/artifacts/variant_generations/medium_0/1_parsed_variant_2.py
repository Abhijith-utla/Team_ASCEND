def sat(lst: List[str]):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
