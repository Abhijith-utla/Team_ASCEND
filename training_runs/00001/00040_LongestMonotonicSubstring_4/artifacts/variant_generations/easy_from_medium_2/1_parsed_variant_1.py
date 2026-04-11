def sat(x: List[int], s: str):
    return all(s[i] <= s[i + 1] for i in range(len(x) - 1))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
