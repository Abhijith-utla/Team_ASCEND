def sat(s: str):
    return sorted(s) == sorted('sirnemtpu') and s == s[::-1]

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
