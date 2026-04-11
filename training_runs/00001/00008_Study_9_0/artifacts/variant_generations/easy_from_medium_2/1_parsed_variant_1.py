def sat(li: List[str]):
    return all(i.isdigit() for i in li)

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
