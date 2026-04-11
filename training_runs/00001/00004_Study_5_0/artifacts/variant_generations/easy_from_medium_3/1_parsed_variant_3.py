def sat(li: list) -> bool:
    return all([li.count(i) == i for i in range(10)]) == li.count(0) == 1

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
