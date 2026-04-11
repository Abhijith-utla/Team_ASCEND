def sat(s: str):
    return str(int(8 ** 2888) ** 0.5).count(s) > 8 and len(s) == 3

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
