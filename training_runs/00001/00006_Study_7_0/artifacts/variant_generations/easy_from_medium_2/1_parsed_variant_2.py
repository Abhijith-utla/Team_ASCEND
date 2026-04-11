def sat(s: str) -> bool:
    return str(2888 ** int(8)).count(s) > 8 and len(s) == 3

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
