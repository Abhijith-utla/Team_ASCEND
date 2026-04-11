def sat(s: str) -> bool:
    return sorted(s) == sorted('Auipenmtrs') and s == s[::-1]

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
