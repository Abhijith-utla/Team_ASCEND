def sat(x: List[int], s: str):
    return all(s[x[i]] < s[x[i + 1]] for i in range(len(x) - 1))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
