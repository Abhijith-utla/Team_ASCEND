def sat(x: List[int], length=1, s="O!A{SeKv"):
    return all(ord(ch) <= ord(s[x[i]]) for i in range(length))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
