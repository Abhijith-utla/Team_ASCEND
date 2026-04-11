def sat(i: int) -> bool:
    return len(str(i + 10)) == len(str(i + 100))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
