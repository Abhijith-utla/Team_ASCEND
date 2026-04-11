def sat(x: List[int], l: int, s: str):
    return all(s[i] <= s[i + 1] for i in range(l))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
