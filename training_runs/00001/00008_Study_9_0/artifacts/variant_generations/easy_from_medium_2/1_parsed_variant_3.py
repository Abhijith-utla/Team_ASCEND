def sat(li: List[str]):
    return all(len(i) <= 5 for i in li) and all(i.isalpha() for i in li)

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
