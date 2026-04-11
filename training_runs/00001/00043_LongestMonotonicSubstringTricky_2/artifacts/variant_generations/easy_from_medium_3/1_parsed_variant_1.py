def sat(x: List[int], length=1, s="O!A{SeKv"):
    return all(s.count(s[x[i]]) == s.count(s[x[i + 1]]) and x[i + 1] >= x[i] for i in range(length - 1))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
