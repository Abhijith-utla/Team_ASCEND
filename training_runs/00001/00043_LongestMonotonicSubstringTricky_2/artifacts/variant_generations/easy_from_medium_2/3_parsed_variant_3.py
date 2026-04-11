def sat(x: List[int], s="O!A{SeKv"):
    return all(ord(ch) <= ord(s[x[i]]) for i in range(len(x)))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
