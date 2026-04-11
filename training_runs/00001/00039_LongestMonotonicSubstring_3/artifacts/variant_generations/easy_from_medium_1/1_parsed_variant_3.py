def sat(x: List[int], length=0, s=""):
    return all(s[x[i]] > s[x[i + 1]] for i in range(length - 1))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
